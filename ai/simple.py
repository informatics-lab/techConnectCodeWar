import game
import random

PLAYER = 'X'

def getMove():
    return random.randint(0,6);



print(game.state())
game.play(PLAYER, getMove())
print(game.state())
