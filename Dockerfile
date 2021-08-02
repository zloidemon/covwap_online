FROM python:3.9 AS build

WORKDIR /app
COPY . /app

RUN pip install -r requirements-dev.txt
RUN py.test -v -p no:warnings

FROM python:3.9

WORKDIR /app
COPY . /app

ENV COINBASE_HOST "wss://ws-feed-public.sandbox.pro.coinbase.com"
ENV CAPACITY 200
ENV PAIRS "BTC-USD,BTC-USD,ETH-BTC"

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "run.py"]
