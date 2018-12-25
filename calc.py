from cards import functions
from copy import deepcopy
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.cards = []

class Game:
    def __init__(self, names):
        self.names = names
        self.players = [Player(name) for name in self.names]
        self.move_cursor = 0
        self.deck = {
            'assassina': 1,
            'contessa': 1,
            'capitano': 1,
            'ambasciatore': 1,
            'duca': 1,
            'inquisitore': 1,
            'senatore': 1,
            'sabotatore': 1
        }

    def __mover_get(self):
        return self.players[self.move_cursor]

    mover = property(__mover_get)

    def make_move(self):
        self.players = [player for player in self.players if len(player.cards) > 0]

        if len(self.players) > 1:
            winners = []

            for move in self.mover.moves:
                next_game_state = deepcopy(self)
                move(next_game_state)

        else:
            return 

    def blocked_by(self,role):
        for i in range(len(self.players)):
            if not i == self.move_cursor:
                if role in self.players[i].cards:
                    return True
        return False
    
    def draw_card(self):
        card_index = random.randint(1, (sum(self.deck.values())))

        for card_type in self.deck:
            card_index = card_index - self.deck[card_type]

            if card_index <= 0:
                self.deck[card_type] += -1
                return card_type