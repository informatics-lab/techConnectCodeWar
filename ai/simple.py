import game
import random
from random_player import Player

px = Player('x')
po = Player('o')

game.restart()
for i in range(200):
    print(game.state())
    px.play()
    print(game.state())
    po.play()