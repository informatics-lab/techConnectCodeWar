import game
import random

def get_highest_column(data):
    output = [0] * 7
    for row in data[::-1]:
        for i, column in enumerate(row):
            if column != '-':
                output[i] =+ 1
    return max(output).index

def get_shortest_column(data):
    output = [0] * 7
    for row in data[::-1]:
        for i, column in enumerate(row):
            if column != '-':
                output[i] =+ 1
    return output.index(min(output))

def is_top_mine(data):
    i = 0
    for column in data[0]:
        if column == 'O':
            return False
        elif column == 'X':
            return True
        else:
            i += 1

if __name__ == '__main__':
    print(is_top_mine)
