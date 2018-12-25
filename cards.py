from enum import Enum

functions = {
    'tax':          tax_money,
    'foreign_aid':  foreign_aid,
    'assassina':    assassina,
    'capitano':     capitano,
    'ambaciatore':  ambasciatore,
    'duca':         duca,
    'inquisitore':  inquisitore,
    'sabotatore':   sabotatore
}

def tax_money(game):
    game.mover.money += 1

def foreign_aid(game):
    if not game.blocked_by('Duca') and not game.blocked_by('Inquisitor'):
        game.mover.money += 2
    else:
        return 'NOT ALLOWED'

def assassina(game):
    if game.mover.money >= 3:
        for player in game.players:
            if player is not game.mover:
                pass # TODO
    else:
        return 'NOT ALLOWED'

def capitano(game):
    for player in game.players:
        if player is not game.mover:
            pass # TODO

def ambasciatore(game):
    game.mover.cards.append(game.draw_card())
    game.mover.cards.append(game.draw_card())

    pass # TODO: Evaluate game after each potential decision

def duca(game):
    game.mover.money += 3

def inquisitore(game):
    for player in game.players:
        pass # TODO

def sabotatore(game):
    game.mover.money += 2