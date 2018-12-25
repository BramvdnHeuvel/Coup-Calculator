from copy import deepcopy
from calc import Player, Game
import time

deck = {
    'assassina': 2,
    'contessa': 1,
    'capitano': 3,
    'ambasciatore': 3,
    'duca': 2
}

mark = Player("Mark")
mark.cards = ['duca']
mark.money = 0

bram = Player("Bram")
bram.cards = ['contessa', 'ambasciatore']
bram.money = 3

g = Game(["Bram", "Mark"])
g.players = [bram, mark]
g.deck = deck

t = time.time()
results = {"Bram": 0, "Mark": 0}

while time.time() - t < 5:
    results[deepcopy(g).play_game()] += 1

for player in results:
    print(f'{player} - {results[player]*100/sum(results.values())}\%')