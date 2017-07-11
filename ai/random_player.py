from tools import logic
from tools import game

def get_move(player):
    logic.setup(player, game.state())
    move = logic.random_legal_move()
    return move
