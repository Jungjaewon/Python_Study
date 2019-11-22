import datetime
from builtins import print

import time
import json
"""
Book : effective Python
section 20

arg in function, 
each arg is evaluated when the function is firstly called.
Then, when in log does not get change.

"None" is utilized to solve the problem.

"""

def log(msg, when=datetime.datetime.now()):
    print('%s %s' % (when, msg))

def log_right(msg, when=None):
    if when is None:
        when = datetime.datetime.now()
    print('%s %s' % (when, msg))

def log_testing():
    print('-' * 5 + 'log_testing' + '-' * 5)
    log('Logging')
    time.sleep(2)
    log('Logging')

def log_testing_right():
    print('-' * 5 + 'log_testing_right' + '-' * 5)
    log_right('Logging')
    time.sleep(2)
    log_right('Logging')


def json_decode(data, default = {}):
    try:
        return json.loads(data)
    except ValueError:
        return default

def json_decoding():
    print('-' * 5 + 'json_decoding' + '-' * 5)
    A = json_decode('bad example')
    A['one'] = 1
    B = json_decode('Bad two')
    B['two'] = 2
    print('A : ', A)
    print('B : ', B)


def json_decode_right(data, default=None):
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


def json_decoding_right():
    print('-' * 5 + 'json_decoding_right' + '-' * 5)
    A = json_decode_right('bad example')
    A['one'] = 1
    B = json_decode_right('Bad two')
    B['two'] = 2
    print('A : ', A)
    print('B : ', B)


if __name__ == '__main__':
    log_testing()
    log_testing_right()
    json_decoding()
    json_decoding_right()

