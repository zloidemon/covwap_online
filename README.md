Online calculation VWAP
-----------------------

Configuration
-------------

* `COINBASE_HOST` remote websocket
* `CAPACITY` copacity in ring buffer
* `PAIRS` list of pairs BTC-USD,BTC-USD,ETH-BTC

Local running
-------------

```
$ docker build -t covwap_online .
$ docker run -it --rm covwap_online
```
