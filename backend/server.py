# CardsAgainstX - A cards against humanity clone.
# Python Websocket Server
# By InvalidSE - https://github.com/invalidse

# Temp config, while everything is in 1 file lol
max_players = 20
webserver_port = 8765

# This could be a terrible way to do it, but here goes:
games = []

# Game class! Here's how the game data is stored:
class Game:
    def __init__(self, code, packs, custom_cards, host):
        self.custom_cards == custom_cards
        self.code == code
        self.packs == packs
        self.players == [host] # If players[0] disconnects, terminate server? Maybe.

# Player class:
class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cards = []
        self.points = 0

    def add_card(self, cards, number):
        for i in range(number):
            self.cards.append(cards.random())


from websockets.server import serve
import asyncio
from time import sleep

async def main():
    async with serve(handler, "localhost", webserver_port):
        print("[STATUS] Server Initialised")
        await asyncio.Future()

async def handler(websocket):
    async for message in websocket:
        print("[RECIEVED] {message}")
    

if __name__ == "__main__":
    print("[STATUS] Starting Server...")
    asyncio.run(main())

