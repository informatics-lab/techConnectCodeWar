from tools import logic
from tools import game

def get_move(player):
    logic.setup(player, game.state())
    legal_moves = logic.legal_moves()
    move = legal_moves[0]
    return move
