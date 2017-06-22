import game
import random
from random_player import Player
from basic_player import BPlayer

px = BPlayer('x')
po = BPlayer('o')

def play_game(state, player, opposition):

    if player.is_board_empty(state):
        game.play(player.player,3)
        return None

    horizontal_blocks = []
    for column in player.get_legal_moves(state):
        row = player.get_top_of_stack(state, column)
        if opposition.number_player_pieces_to_right(state, column, row + 1) == 3:
            horizontal_blocks.append(column)
        elif opposition.number_player_pieces_to_left(state, column, row + 1) == 3:
            horizontal_blocks.append(column)

    vertical_blocks = []
    for column in player.get_legal_moves(state):
        if opposition.number_player_pieces_top_of_column(state, column) == 3:
            vertical_blocks.append(column)

    horizontal_wins = []
    for column in player.get_legal_moves(state):
        row = player.get_top_of_stack(state, column)
        if player.number_player_pieces_to_right(state, column, row + 1) == 3:
            horizontal_wins.append(column)
        elif player.number_player_pieces_to_left(state, column, row + 1) == 3:
            horizontal_wins.append(column)

    vertical_wins = []
    for column in player.get_legal_moves(state):
        if player.number_player_pieces_top_of_column(state, column) == 3:
            vertical_wins.append(column)

    if horizontal_wins:
        game.play(player.player, random.choice(horizontal_wins))
        return None
    if vertical_wins:
        game.play(player.player, random.choice(vertical_wins))
        return None

    if horizontal_blocks:
        game.play(player.player, random.choice(horizontal_blocks))
        return None
    if vertical_blocks:
        game.play(player.player, random.choice(vertical_blocks))
        return None

    top_of_column_stacks = []
    for column in player.get_legal_moves(state):
        top_of_column_stacks.append(player.number_player_pieces_top_of_column(state, column))
    tallest_stack = top_of_column_stacks.index(max(top_of_column_stacks))
    game.play(player.player, tallest_stack)
    return None

play_game(game.state(), px, po)
game.print_state()

play_game(game.state(), po, px)

game.print_state()
