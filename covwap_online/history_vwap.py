# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4:

from decimal import Decimal
import numpy as np
from numpy_ringbuffer import RingBuffer


class HistoryVWAP:
    def __init__(self, product, capacity):
        self.product = product
        self.capacity = capacity
        self.__rb = RingBuffer(capacity=capacity, dtype=np.ndarray)
        self.__func_numerator = np.vectorize(lambda v: v[0] * v[1])
        self.__func_denominator = np.vectorize(lambda v: v[1])
        self.__seqnum = 0

    def append(self, seqnum, price, quantity):
        if not isinstance(price, Decimal):
            raise Exception("price has wrong type")
        if not isinstance(quantity, Decimal):
            raise Exception("quantity has wrong type")
        if not isinstance(seqnum, int):
            raise Exception("seqnum has wrong type")
        if seqnum <= self.__seqnum:
            raise Exception("wrong sequence number")

        self.__seqnum = seqnum
        self.__rb.append(np.array([price, quantity]))

    @property
    def data(self):
        return np.array(self.__rb)

    def __calc(self):
        return self.__func_numerator(self.data).sum() / \
            self.__func_denominator(self.data).sum()

    @property
    def result(self):
        if not self.__rb.is_full:
            return False, len(self.__rb)
        return True, self.__calc()

    @property
    def result_force(self):
        return self.__calc()

    def __len__(self):
        return len(self.__rb)

    def __repr__(self):
        return f"<HistoryVWAP(capacity={self.capacity})>"
