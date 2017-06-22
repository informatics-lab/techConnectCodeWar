from urllib import request
import json

def __api(path, method=None):
    base_url = 'http://52.213.11.19:3000/conn4/api/'
    response = request.urlopen(request.Request(base_url + path, method=method))
    return json.load(response)


def state():
    return __api('state')

def play(player, col):
    player = player.lower()
    assert player == 'x' or player == 'o'
    assert 0 <= col <= 6
    assert isinstance(col, int)
    return __api('play/' + player + '/' + str(col), method="PUT")

def restart():
    return __api('reset', method='PUT')


if __name__ == "__main__":
    print(restart())
    print(state())
    print(play('X', 1))
    print(state())
    print(play('O', 1))
    print(play('X', 0))
    print(state())
    print(restart())
    print(state())