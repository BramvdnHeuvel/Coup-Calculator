from enum import Enum
import random

def random_move(self):
    mover = self.mover
    possible_moves = []

    if mover.money >= 7:
        for target in self.players:
            if target is not mover:
                for card in target.cards:
                    possible_moves.append(functions['coup'](target, card))

    if mover.money < 10:
        possible_moves.append(functions['tax'])
        if not self.blocked_by('duca') and not self.blocked_by('inquisitore'):
            possible_moves.append(functions['foreign_aid'])

        if 'assassina' in mover.cards:
            for i in range(20):
                target = random.choice(self.players)
                if target is not mover and 'contessa' not in target.cards:
                    card = random.choice(target.cards)
                    possible_moves.append(functions['assassina'](target, card))
                    break
        
        if 'capitano' in mover.cards:
            for i in range(20):
                target = random.choice(self.players)
                if 'capitano' not in target.cards and 'ambasciatore' not in target.cards and target.money > 0:
                    possible_moves.append(functions['capitano'](target))
                    break
        
        if 'ambasciatore' in mover.cards:
            possible_moves.append(functions['ambasciatore'])
        
        if 'duca' in mover.cards:
            possible_moves.append(functions['duca'])
        
        if 'inquisitore' in mover.cards:
            target = random.choice(self.players)
            card = random.choice(target.cards)
            possible_moves.append(functions['inquisitore'](target, card))
        
        if 'sabotatore' in mover.cards:
            possible_moves.append(functions['sabotatore'])
    
    random.choice(possible_moves)(self)
    return self

def coup(target, card):
    def coup(game):
        target.cards.remove(card)
        game.mover.money += -7
    return coup

def tax_money(game):
    game.mover.money += 1

def foreign_aid(game):
    game.mover.money += 2

def assassina(target, card):
    def assassina(game):
        target.cards.remove(card)
        game.mover.money += -3
    return assassina

def capitano(target):
    def capitano(game):
        money_to_steal    = min(2, target.money)
        target.money     += -money_to_steal
        game.mover.money += money_to_steal
    return capitano

def ambasciatore(game):
    game.mover.cards.append(game.draw_card())
    game.mover.cards.append(game.draw_card())
    
    chosen_cards = random.sample(game.mover.cards, 2)

    for card in game.mover.cards:
        game.deck[card] += 1

    for card in chosen_cards:
        game.deck[card] += -1
    
    game.mover.cards = chosen_cards

def duca(game):
    game.mover.money += 3

def inquisitore(target, card):
    def inquisitore(game):
        pass # TODO
    
    return inquisitore

def sabotatore(game):
    game.mover.money += 2

functions = {
    'coup':         coup,
    'tax':          tax_money,
    'foreign_aid':  foreign_aid,
    'assassina':    assassina,
    'capitano':     capitano,
    'ambasciatore':  ambasciatore,
    'duca':         duca,
    'inquisitore':  inquisitore,
    'sabotatore':   sabotatore
}