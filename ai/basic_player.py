import game
import numpy as np

class BPlayer(object):
    def __init__(self, player):
        self.player = player.upper()
        self.opposition = 'x' if player == 'o' else 'x'

    def make_random_choice(self, state):
        return random.choice(self.get_legal_moves(state))

    def get_column_info(self, state):
        output = [0] * 7
        xs = [0] * 7
        os = [0] * 7
        for row in state[::-1]:
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

    def get_top_of_stack(self, state, column):
        # return the index for the row at the top of a stack
        return self.get_column_info(state)[0][column] - 1

    def get_legal_moves(self, state):
        # return a list of numbers
        # corresponding to indices of columns where a piece can be placed
        i = 0
        moves = []
        for column in state[0]:
            if column == '-':
                moves.append(i)
            i += 1
        return moves

    def is_board_empty(self, state):
            # return true if no pieces on board
        if state[-1].strip() == '-' * 7:
            return True
        else:
            return False

    def is_column_full(self, state, column):
        # for a given column, test if the column is full
        # return true/false
        if state[0][column] == '-': # data[0] corresponds to top row of board
            # if top row of column is a dash ie column not full
            return False
        else:
            # else column is full
            return True

    def number_player_pieces_top_of_column(self, state, column):
        # return the number of player pieces at the top of a given column
        count = 0
        column_height = self.get_column_info(state)[0][column]
        flipped_state = np.flipud(state) # make bottom row the 0th row
        for row in range(column_height-1,-1,-1):
            # loop from top of column to bottom
            if flipped_state[row][column] == self.player:
                count += 1
            else:
                # loop stops at first piece that isn't a player piece
                break
        return count

    def is_square_empty(self, state, column, row):
        # test if a given square is empty
        if np.flipud(state)[row][column] == '-':
            return True
        else:
            return False

    def number_player_pieces_to_right(self, state, column, row):
        # return the number of player pieces consecutive to a square (on right)
        count = 0
        if column == 6:
            return count
        flipped_state = np.flipud(state)
        if flipped_state[row][column+1] == self.player:
            count += 1
            count += self.number_player_pieces_to_right(state, column + 1, row)
            return count
        else:
            return count

    def number_player_pieces_to_left(self, state, column, row):
        # return the number of player pieces consecutive to a square (on left)
        count = 0
        if column == 0:
            return count
        flipped_state = np.flipud(state)
        if flipped_state[row][column-1] == self.player:
            count += 1
            count += self.number_player_pieces_to_left(state, column - 1, row)
            return count
        else:
            return count
