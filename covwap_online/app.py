# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4:

import json
from decimal import Decimal
import websockets

from .history_vwap import HistoryVWAP


SUPPORTED_PRODUCTS = (
    "BTC-USD",
    "ETH-BTC",
    "ETH-USD",
)

class App:
    def __init__(self, uri, products, capacity, history):
        self.products = products
        self.__uri = uri
        self.history = history
        self.capacity = capacity

    def process(self, raw_data):
        data = json.loads(raw_data)

        if data["type"] == "error":
            raise Exception(f'{data["message"]}: {data["reason"]}')

        if data["type"] in ["last_match", "match"]:
            product_id = data["product_id"]

            if product_id in self.products:
                quantity = Decimal(data["size"])
                price = Decimal(data["price"])
                seqnum = data["sequence"]
            else:
                raise Exception(f"Product not found: {product_id}")

            history = self.history[product_id]
            history.append(seqnum, price, quantity)

            status, result = history.result

            if status:
                return product_id, result

            return product_id, f"bootstrap {result}/{self.capacity} " \
                f"force now: {history.result_force}"
        return None, None

    async def run(self):
        async with websockets.connect(self.__uri) as websocket:
            await websocket.send(json.dumps({
                "type": "subscribe",
                "product_ids": self.products,
                "channels": ["matches"],
            }))

            while True:
                try:
                    raw_data = await websocket.recv()
                    product, result = self.process(raw_data)

                    if result:
                        print(f"vwap: {product}: {result}")
                except:
                    raise Exception("failed on getting data from socket")

    @classmethod
    def create(cls, uri, products, capacity):
        if not isinstance(products, list):
            raise Exception("products should be list")

        for p in products:
            if p not in SUPPORTED_PRODUCTS:
                raise Exception("defined unsupported product")

        history = {k: HistoryVWAP(k, capacity) for k in products}

        return cls(uri, products, capacity, history)
