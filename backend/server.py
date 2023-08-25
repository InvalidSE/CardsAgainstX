# CardsAgainstX - A cards against humanity clone.
# Python Websocket Server
# By InvalidSE - https://github.com/invalidse

from websockets.server import serve
import asyncio

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()

async def echo(websocket):
    async for message in websocket:
        print("[MESSAGE]", message)
        await websocket.send(message)

if __name__ == "__main__":
    print("[STATUS] Starting Server...")
    asyncio.run(main())
