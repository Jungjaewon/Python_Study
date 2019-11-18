from functools import reduce

"""
Ref 1 : https://wayhome25.github.io/cs/2017/04/03/cs-03/
Ref 2 : https://3months.tistory.com/338
Ref 3 : http://seorenn.blogspot.com/2018/08/python3-filter-map-reduce.html
"""
"""
lambda args... :  expresion with args
The function works on heap area and looks an instance function.

map(function, iterable)
- can recude memory because lazy computation
- makes a generator in Python

filter(function, iterable)
- function return type must be bool(T or F)
- 


reduce(function, iterable, [. initializer])
- In Python, the function is not inbuilt function
"""

def lambda_example():
    print('-' * 5 + 'lambda_example' + '-' * 5)
    sum = lambda a,b: a + b
    #lambda args...: expresion with args
    print('sum(1,2) : ', sum(1,2))
    print('sum(3,4) : ', sum(3,4))


def map_example():
    print('-' * 5 + 'map_example' + '-' * 5)
    li = [1, 2, 3]
    result = map(lambda i: i * i, li)
    print('li : ', li)
    print('result = map(lambda i: i * i, li)')
    print('[v * 2 for v in li] also possible')
    print('next(result) : ', next(result))  # 1
    print('next(result) : ', next(result))  # 4
    print('next(result) : ', next(result))  # 9
    #print('next(result) : ', next(result))  # StopIteration 발생


def filter_example():
    print('-' * 5 + 'filter_example' + '-' * 5)
    li = [-2, -3, 5, 6]

    def positive(x):
        return x > 0
    print("li : ", li)
    print('list(filter(positive, li)) : ', list(filter(positive, li)))
    print('list(filter(lambda x: x > 0, li)) : ', list(filter(lambda x: x > 0, li)))
    print('[v for v in li if v > 2 == 0] : ', [v for v in li if v > 2 == 0])


def reduce_example():
    print('-' * 5 + 'reduce_example' + '-' * 5)
    li = [-2,-3,5,6]
    print('reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]) : ', reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])) # sum
    print('sum_value = reduce((lambda x,y : x+y), [x for x in range(1,101)]) is also possible')
    print('reduce(lambda a,b: a if a > b else b ,li) : ', reduce(lambda a,b: a if a > b else b ,li)) # finding max value
    a = reduce(lambda a, b: a if a > b else b, li)
    print('a = reduce(lambda a, b: a if a > b else b, li)')
    print('type(a) : ', type(a))

if __name__ == '__main__':
    lambda_example()
    map_example()
    filter_example()
    reduce_example()

