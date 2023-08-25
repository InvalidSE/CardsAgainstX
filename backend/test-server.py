#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect

def hello():
    with connect("ws://localhost:8765") as websocket:
        websocket.send("Hello world!")
        print("Sent")
    print('Disconnected')

while True:
    input()
    hello()