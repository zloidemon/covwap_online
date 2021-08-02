import unittest
from decimal import Decimal
from covwap_online import App

API_URI = "wss://ws-feed-public.sandbox.pro.coinbase.com"
payload = (
    '{"type":"last_match","trade_id":32229733,"maker_order_id":"846893fc-fe64-43c4-810c-be6c1f2fb715","taker_order_id":"4b6e2af3-a78c-4406-9a2e-d1b28ed8b147","side":"sell","size":"0.00123452","price":"40300","product_id":"BTC-USD","sequence":363455727,"time":"2021-08-01T23:00:03.478824Z"}',
    '{"type":"match","trade_id":32229734,"maker_order_id":"8c978f41-c35b-4af8-9465-2ef1e5a6b643","taker_order_id":"493dc98a-7b86-42d2-84f1-7b812dd08dee","side":"buy","size":"0.00024813","price":"40299.98","product_id":"BTC-USD","sequence":363455736,"time":"2021-08-01T23:00:07.968029Z"}',
    '{"type":"match","trade_id":32229735,"maker_order_id":"846893fc-fe64-43c4-810c-be6c1f2fb715","taker_order_id":"a1506a7d-0da7-4119-a237-eeaef117a7f6","side":"sell","size":"0.00024776","price":"40300","product_id":"BTC-USD","sequence":363455749,"time":"2021-08-01T23:00:13.760870Z"}',
    '{"type":"match","trade_id":32229736,"maker_order_id":"aa015913-113c-4d3a-a16b-a364b90c0835","taker_order_id":"2445e6f2-5c16-4a44-b9fe-a7fba237018d","side":"buy","size":"0.00024864","price":"40218.07","product_id":"BTC-USD","sequence":363455808,"time":"2021-08-01T23:00:18.752677Z"}',
    '{"type":"match","trade_id":32229737,"maker_order_id":"b8fbae70-777e-4690-82a5-c24f430f192b","taker_order_id":"e301b9c8-ab9a-4d72-bcd7-c12f07c830d4","side":"sell","size":"0.00024827","price":"40218.09","product_id":"BTC-USD","sequence":363455813,"time":"2021-08-01T23:00:23.744821Z"}',
    '{"type":"match","trade_id":32229738,"maker_order_id":"aa015913-113c-4d3a-a16b-a364b90c0835","taker_order_id":"20a34491-d377-486d-8508-4a90c4fd924e","side":"buy","size":"0.00024864","price":"40218.07","product_id":"BTC-USD","sequence":363455816,"time":"2021-08-01T23:00:28.744473Z"}',
    '{"type":"match","trade_id":32229739,"maker_order_id":"b8fbae70-777e-4690-82a5-c24f430f192b","taker_order_id":"4bdc0d27-f2ee-4bd4-9003-93aaaa1c906b","side":"sell","size":"0.00024827","price":"40218.09","product_id":"BTC-USD","sequence":363455822,"time":"2021-08-01T23:00:33.750024Z"}',
    '{"type":"match","trade_id":32229740,"maker_order_id":"aa015913-113c-4d3a-a16b-a364b90c0835","taker_order_id":"a5ea31e8-cddf-4bc8-850e-859e4b26c14b","side":"buy","size":"0.00024864","price":"40218.07","product_id":"BTC-USD","sequence":363455825,"time":"2021-08-01T23:00:38.755335Z"}',
    '{"type":"match","trade_id":32229741,"maker_order_id":"7f9d94cc-3c16-4f86-bbe2-74d0b2823308","taker_order_id":"65cc8eaf-3106-44f2-b83c-f890c34c2010","side":"sell","size":"0.00024833","price":"40208.47","product_id":"BTC-USD","sequence":363455866,"time":"2021-08-01T23:00:43.744604Z"}',
    '{"type":"match","trade_id":32229742,"maker_order_id":"aa9d3b4d-11d2-4696-a3f9-0dd6811f66cf","taker_order_id":"4fd35c28-9cb7-4f10-b7c4-86c77c934507","side":"buy","size":"0.0002487","price":"40208.45","product_id":"BTC-USD","sequence":363455890,"time":"2021-08-01T23:00:47.952395Z"}',
    '{"type":"match","trade_id":32229743,"maker_order_id":"7f9d94cc-3c16-4f86-bbe2-74d0b2823308","taker_order_id":"eb1b1b59-b831-4300-b4f5-9db0f2360711","side":"sell","size":"0.00024833","price":"40208.47","product_id":"BTC-USD","sequence":363455893,"time":"2021-08-01T23:00:52.976032Z"}',
    '{"type":"match","trade_id":32229744,"maker_order_id":"aa9d3b4d-11d2-4696-a3f9-0dd6811f66cf","taker_order_id":"c16fcf71-1c80-4d2a-beba-a96a0a8316fc","side":"buy","size":"0.0002487","price":"40208.45","product_id":"BTC-USD","sequence":363455896,"time":"2021-08-01T23:00:57.939706Z"}',
    '{"type":"match","trade_id":32229745,"maker_order_id":"7f9d94cc-3c16-4f86-bbe2-74d0b2823308","taker_order_id":"39131bb1-dc2e-4bd9-85ff-5bba276ce6bf","side":"sell","size":"0.00024833","price":"40208.47","product_id":"BTC-USD","sequence":363455902,"time":"2021-08-01T23:01:02.958191Z"}',
    '{"type":"match","trade_id":32229746,"maker_order_id":"aa9d3b4d-11d2-4696-a3f9-0dd6811f66cf","taker_order_id":"0253b3cf-3c61-4427-a360-f464502cfa15","side":"buy","size":"0.02830507","price":"40208.45","product_id":"BTC-USD","sequence":363455905,"time":"2021-08-01T23:01:06.958663Z"}',
    '{"type":"match","trade_id":32229747,"maker_order_id":"aa9d3b4d-11d2-4696-a3f9-0dd6811f66cf","taker_order_id":"1a00a84a-56ea-48ea-8968-b1cdc45fa1f0","side":"buy","size":"0.0002487","price":"40208.45","product_id":"BTC-USD","sequence":363455908,"time":"2021-08-01T23:01:07.941042Z"}',
    '{"type":"match","trade_id":32229748,"maker_order_id":"7f9d94cc-3c16-4f86-bbe2-74d0b2823308","taker_order_id":"f2e63cd7-fb5a-4ae3-878a-110fdbc7964e","side":"sell","size":"0.00024833","price":"40208.47","product_id":"BTC-USD","sequence":363455911,"time":"2021-08-01T23:01:13.571443Z"}',
    '{"type":"match","trade_id":32229749,"maker_order_id":"7886e673-6f85-4fe4-8b0b-789263342a1b","taker_order_id":"82dd684f-20f7-4961-b146-1c152dd5a661","side":"buy","size":"0.0002485","price":"40241.42","product_id":"BTC-USD","sequence":363455969,"time":"2021-08-01T23:01:18.557989Z"}',
)

class TestClient(unittest.TestCase):

    def setUp(self):
        self.capacity = 10

    def test_create(self):
        App.create(API_URI, ["BTC-USD"], self.capacity)

        with self.assertRaises(Exception):
            App.create(API_URI, ["XXX-XXX"], self.capacity)

    def test_process(self):
        app = App.create(API_URI, ["BTC-USD"], self.capacity)
        for num, d in enumerate(payload):
            if num < self.capacity - 1:
                self.assertIn('bootstrap', app.process(d)[1])

    def test_process_wrong_product(self):
        app = App.create(API_URI, ["BTC-USD"], self.capacity)
        with self.assertRaises(Exception):
            app.process('{"type":"match","trade_id":32229739,"maker_order_id":"b8fbae70-777e-4690-82a5-c24f430f192b","taker_order_id":"4bdc0d27-f2ee-4bd4-9003-93aaaa1c906b","side":"sell","size":"0.00024827","price":"40218.09","product_id":"XXX-XXX","sequence":363455822,"time":"2021-08-01T23:00:33.750024Z"}')

    def test_process_wrong_pair(self):
        app = App.create(API_URI, ["BTC-USD"], self.capacity)
        with self.assertRaises(Exception):
            app.process('{"type":"error","message":"Failed to subscribe","reason":"XXX is not a valid product"}')

    def test_get_vwap(self):
        app = App.create(API_URI, ["BTC-USD"], self.capacity)
        for d in payload:
            x = app.process(d)
        self.assertEqual(("BTC-USD", Decimal('40208.79722535110274075090295'),), x)
