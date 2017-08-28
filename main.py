# --*-- encoding: utf -8 --*--

from urllib import request, parse
import time
import json
from strategy import choice

url = 'https://httpbin.org/post'  # Set destination URL here
_stragety = choice.choiceBase()

def sendDataToServer(dct_data):
    req = request.Request(url, parse.urlencode(dct_data).encode())
    rsp = request.urlopen(req).read().decode()
    return rsp

def processResponseFromServer(str_response):
    dct_response = json.loads(str_response)
    data = _stragety.getNextStep(dct_response)
    return data

if __name__ == '__main__':
    i = 0
    _data = {
        'a': '1'
    }
    while (True):
        i += 1
        rsp = sendDataToServer(_data)
        print('========{0}==========='.format(str(i)))
        print(rsp)
        _data = processResponseFromServer(rsp)
        time.sleep(5)
