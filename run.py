# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4:

import asyncio
import sys
import os

from covwap_online import App

try:
    COINBASE_HOST = os.environ['COINBASE_HOST']
    CAPACITY = int(os.environ['CAPACITY'])
    PAIRS = os.environ['PAIRS'].strip().split(',')
except:
    print('failed on start')
    sys.exit(1)

app = App.create(
    COINBASE_HOST,
    PAIRS,
    CAPACITY,
)
asyncio.get_event_loop() \
    .run_until_complete(app.run())
