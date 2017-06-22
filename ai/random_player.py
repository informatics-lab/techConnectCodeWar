import random
import game

class Player(object):
    def __init__(self, player):
        self.player = player.upper()
        self.opposition = 'X' if player == 'O' else 'X'

    def play(self):
        col = random.randint(0, 6)
        game.play(self.player, col)
