
import time

# https://jupiny.com/2016/09/25/decorator-function/
def one(function):
    def wrapper(*args, **kwargs):
        print("function one start")
        ret = function(*args, **kwargs)
        print("function one end")
        return ret
    return wrapper

def two(function):
    def wrapper(*args, **kwargs):
        print("function two start")
        ret = function(*args, **kwargs)
        print("function two end")
        return ret
    return wrapper

def three(function):
    def wrapper(*args, **kwargs):
        print("function three start")
        ret = function(*args, **kwargs)
        print("function three end")
        return ret
    return wrapper

@one
@two
@three
def something():
    print("function something")

def get_timer_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        print(result)
        end_time = time.time()
        print("실행시간은 {time}초 입니다.".format(time=(end_time - start_time)))
        return result
    return wrapper

@get_timer_decorator
def fibonacci_iterative(n):
    prev_n, cur_n = 0, 1
    i = 1

    while i < n:
        cur_n, prev_n = cur_n + prev_n, cur_n
        i+=1
    return cur_n


if __name__ == '__main__':
    fibonacci_iterative(10)

    something()
    """
    function one start
    function two start
    function three start
    function something 본 함수는 한번 박에 실행되지 않는다.
    function three end
    function two end
    function one end
    """