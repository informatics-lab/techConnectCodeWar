from . import game
import numpy as np # TODO: Can we live without?
import random

ME = '-'
THEM = '-'
STATE = None

def setup(player, state):
    """
    Set up which player (X or O) the AI should play as and the state of the board.
    Needs to be called before any of the other functions.
    Needs to be recalled when the board state changes (i.e. after a play.)
    """
    global ME
    global THEM
    global STATE

    player = player.upper()
    assert player == 'X' or player == 'O'
    ME = player
    THEM = 'O' if player is 'X' else 'X'
    assert state
    STATE = state


def random_legal_move():
    """
    Return a random legal move.
    """
    return random.choice(legal_moves())

def legal_moves():
    """
    Return a list of all the avaliable legal moves.
    """
    i = 0
    moves = []
    for column in STATE[0]:
        if column == '-':
            moves.append(i)
        i += 1
    return moves

def board_is_empty():
    """
    Return True if no pieces have yet been played.
    """
    if STATE[-1].strip() == '-' * 7:
        return True
    else:
        return False

def is_column_full(column):
    """
    Is the column `column` full?
    """
    if STATE[0][column] == '-': # data[0] corresponds to top row of board
        # if top row of column is a dash ie column not full
        return False
    else:
        # else column is full
        return True

def number_of_my_pieces_on_top_of_column(column):
    """
    Returns the number of your pieces are consecutively stacked on to of column 'column'
    """
    return number_pieces_on_top_of_column(column, ME)

def number_of_their_pieces_on_top_of_column(column):
    """
    Returns the number of their pieces are consecutively stacked on to of column 'column'
    """
    return number_pieces_on_top_of_column(column, THEM)

def number_pieces_on_top_of_column(column, type):
    """
    How many pieces of type 'type' are consecutively stacked on to of column 'column'
    """
    count = 0
    column_height =  __get_top_of_stack(column)
    flipped_state = np.flipud(STATE) # make bottom row the 0th row
    for row in range(column_height-1,-1,-1):
        # loop from top of column to bottom
        if flipped_state[row][column] == type:
            count += 1
        else:
            # loop stops at first piece that isn't a piece or type 'type'
            break
    return count

def square_empty(column, row):
    """
    Is a cell empty.
    """
    if np.flipud(STATE)[row][column] == '-':
        return True
    else:
        return False

def number_of_my_pieces_to_left(column):
    """
    Return the number of your consecutive pieces to the left of the avaliable move in column 'column' 
    """
    row = __get_top_of_stack(column)
    return number_pieces_of_type_in_direction(column, row, ME, 'left')

def number_of_my_pieces_to_right(column):
    """
    Return the number of your consecutive pieces to the right of the avaliable move in column 'column' 
    """
    row = __get_top_of_stack(column)
    return number_pieces_of_type_in_direction(column, row, ME, 'right')

def number_of_their_pieces_to_left(column):
    """
    Return the number of their consecutive pieces to the left of the avaliable move in column 'column' 
    """
    row = __get_top_of_stack(column)
    return number_pieces_of_type_in_direction(column, row, THEM, 'left')

def number_of_their_pieces_to_right(column):
    """
    Return the number of their consecutive pieces to the right of the avaliable move in column 'column' 
    """
    row = __get_top_of_stack(column)
    return number_pieces_of_type_in_direction(column, row, THEM, 'right')

def number_pieces_of_type_in_direction(column, row, type, direction):
    """
    Return the number of consecutive pieces of 'type' in direction 'direction' from cell ('column', 'row')
    
    column:     0-6 column in the game
    row:        0-5 row in the game
    type:       'X' or 'O'
    direction:  'left' or 'right'
    """
    # return the number of player pieces consecutive to a square (on left)
    count = 0
    end_col = 0 if direction == 'left' else 6
    col_index_inc = 1 if direction == 'right' else -1
    if column == end_col:
        return count
    flipped_state = np.flipud(STATE)
    if flipped_state[row][column + col_index_inc] == type:
        count += 1
        count += number_pieces_of_type_in_direction(column + col_index_inc, row, type, direction)
        return count
    else:
        return count



def __get_column_info():
    output = [0] * 7
    xs = [0] * 7
    os = [0] * 7
    for row in STATE[::-1]:
        for i, column in enumerate(row.strip()):
            # count the height of pieces in the column
            if column != '-':
                output[i] += 1
                # count the number of Xs in the column
                if column == "X":
                    xs[i] += 1
                # count the number of 0s in the column
                elif column == "O":
                    os[i] += 1
    return output, xs, os


def __get_top_of_stack(column):
    # return the index for the row at the top of a stack
    return __get_column_info()[0][column] - 1