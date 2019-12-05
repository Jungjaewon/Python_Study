from functools import wraps
# Ref1 : https://nachwon.github.io/decorator/
"""
This example talk about several decorators.
the order of decorator is important

"""

def say_hello(func):
    @wraps(func) # this command keeps the original function'names properly
    def wrapper(*args, **kwargs):
        print('Hello')
        return func(*args, **kwargs)
    return wrapper


def say_hi(func):
    @wraps(func) # this command keeps the original function'names properly
    def wrapper(*args, **kwargs):
        print('Hi')
        return func(*args, **kwargs)
    return wrapper

"""
introduce = say_hi(introduce)
introduce = say_hello(introduce)
"""
# @say_hi # we can add more duplicate decorator
@say_hello
@say_hi
def introduce(name):
    print(f'My name is {name}!')


if __name__ == '__main__':
    introduce('Jaewon')
    print("introduce : ", introduce)
    print("introduce.__wrapped__ : ", introduce.__wrapped__)
    print("dir(introduce) : ", dir(introduce))
    print("dir(introduce.__wrapped__) : ",dir(introduce.__wrapped__))
    print("dir(introduce.__wrapped__.__wrapped__) : ",dir(introduce.__wrapped__.__wrapped__))
    #print("dir(introduce.__wrapped__.__wrapped__.__wrapped__) : ",dir(introduce.__wrapped__.__wrapped__.__wrapped__))
    # This statement makes an error. because two decorator are used on the introduce funciton.

