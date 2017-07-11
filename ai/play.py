import fill_up_column_player
import random_player
from tools import game

game.restart()
for i in range(20):
    # X's go
    
    move = random_player.get_move('X')
    game.play('X', move)

    print("X goes in col", move)
    game.print_state()

    # O's move
    move = fill_up_column_player.get_move('O')
    game.play('O', move)


    print("O goes in col", move)
    game.print_state()
