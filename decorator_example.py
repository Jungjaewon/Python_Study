from functools import wraps
# Ref 1 : https://nachwon.github.io/decorator/
# Ref 2 : https://wikidocs.net/23106
# Ref 3 : https://whatisthenext.tistory.com/113
"""
This example is about python's decorator basic

Decorator does not touch an original function.

"""

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Hello')
        return func(*args, **kwargs)
    return wrapper # wraps(func)(wrapper)

"""
@wraps(func)
wraps(func)(wrapper) 
Those prevent an original function information loss.
origin_func.name 
"""


def introduce(name):
    print(f'My name is {name}!')


@decorator # @decorator_name
def introducing(name):
    print(f'My name is {name}!')

def make_cal(op):
    if op == '+':
        return lambda x, y : x + y
    if op == '-':
        return lambda x, y : x - y
    if op == '*':
        return lambda x, y : x * y
    if op == '/':
        return lambda x, y : x / y

"""
make_cal function is almost same as sum = lambda x,y : x + y
"""


def check_func_name(func):
    #print('function name : ', func.__name__)
    return func.__name__


if __name__ == '__main__':
    print('-' * 5 + 'decorator_example1' + '-' * 5)
    decorated_introduce = decorator(introduce)
    decorated_introduce('Jaewon')
    print('decorated_introduce : ', decorated_introduce)

    print('-' * 5 + 'decorator_example2' + '-' * 5)
    introducing('Jake')

    print('-' * 5 + 'function_name_example' + '-' * 5)
    print('check_func_name(intorduce) : ', check_func_name(introducing))

