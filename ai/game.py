import urllib2
import json


class __MethodRequest(urllib2.Request):
    def __init__(self, *args, **kwargs):
        if 'method' in kwargs:
            self._method = kwargs['method']
            del kwargs['method']
        else:
            self._method = None
        return urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self, *args, **kwargs):
        if self._method is not None:
            return self._method
        return urllib2.Request.get_method(self, *args, **kwargs)


def __api(path, method=None):
    base_url = 'http://52.213.11.19:3000/conn4/api/'
    response = urllib2.urlopen(__MethodRequest(base_url + path, method=method))
    return json.load(response)


def state():
    return __api('state')

def play(player, col):
    player = player.lower()
    assert player == 'x' or player == 'o'
    assert 0 <= col <= 6
    assert isinstance(col, (int, long))
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
