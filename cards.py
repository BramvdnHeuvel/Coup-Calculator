from enum import Enum

functions = {
    'coup':         coup,
    'tax':          tax_money,
    'foreign_aid':  foreign_aid,
    'assassina':    assassina,
    'capitano':     capitano,
    'ambaciatore':  ambasciatore,
    'duca':         duca,
    'inquisitore':  inquisitore,
    'sabotatore':   sabotatore
}

def moves(self):
    mover = self.mover

    if mover.money >= 7:
        for target in self.players:
            if target is not mover:
                for card in target.cards:
                    yield functions['coup'](target, card)

    if mover.money < 10:
        yield functions['tax']
        if not self.blocked_by('duca') and not self.blocked_by('inquisitore'):
            yield functions['foreign_aid']

        if 'assassina' in mover.cards:
            for target in self.players:
                if target is not mover and 'contessa' not in target.cards:
                    for card in target.cards:
                        yield functions['assassin'](target, card)
        
        if 'capitano' in mover.cards:
            for target in self.players:
                if 'capitano' not in target.cards and 'ambasciator' not in target.cards and target.money > 0:
                    yield functions['capitano'](target)
        
        if 'ambasciator' in mover.cards:
            for option in functions['ambasciator'](self):
                yield option
        
        if 'duca' in mover.cards:
            yield functions['duca']
        
        if 'inquisitore' in mover.cards:
            for target in self.players:
                for card in target.cards:
                    for choice in functions['inquisitore'](target, card):
                        yield choice
        
        if 'sabotatore' in mover.cards:
            yield functions['sabotatore']

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
    def ambasciatore(card1, card2, others):
        def ambasciatore(game):
            # Shuffle other cards back into the deck.
            others.remove(card1)
            others.remove(card2)
            for card in others:
                game.deck[card] += 1

            # Assign chosen cards to player.
            game.mover.cards = [card1, card2]
        return ambasciatore

    full_list = game.mover.cards
    full_list.append(game.draw_card())
    full_list.append(game.draw_card())

    list_length = len(full_list)
    for i in range(list_length-1):
        for j in range(i+1, list_length):
            yield ambasciatore(full_list[i], full_list[j], full_list)

def duca(game):
    game.mover.money += 3

def inquisitore(target, card):
    def inquisitore(game):
        pass # TODO
    
    return inquisitore

def sabotatore(game):
    game.mover.money += 2