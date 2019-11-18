
"""
Ref 1 : https://arsviator.blogspot.com/2015/04/bytearray-bytearray-object-in-python.html
Ref 2 : https://umbum.tistory.com/268
Ref 3 : https://www.geeksforgeeks.org/python-bytearray-function/

"""

"""
bytes, byrearray can have 0 ~ 255
bytes is not mutable
bytearray is mutable
bytearray works like list with append, insert, find, count, slicing and so on.


bytearray(source, encoding, errors)
bytes(source, encoding, errors)
"""
from builtins import print


def bytes_bytearray():
    print('-' * 5 + 'bytes_bytearray' + '-' * 5)
    data = b'abcd'
    #data = [0,1,2,3,4,5]
    # list and string can be adopted
    x = bytes(data)
    y = bytearray(data)

    print("x[0] : " + str(x[0]))
    # x[0] = ord('b') # this statement makes error
    # x[0] = ord('b') # this statement makes error
    for item in x:
        print(str(item) + ' ', end='')
    print()
    y[0] = ord('d') # bytearray can be mutable
    for item in y:
        print(str(item) + ' ', end='')


def bytearray_examples():
    print('-' * 5 + 'bytearray_examples' + '-' * 5)
    data = b'abcd'
    # data = [0,1,2,3,4,5]
    # list and string can be adopted

    x = bytearray(data)
    y = bytearray(data)
    vals = bytearray()

    print('slicing : ', x[0:2])
    print('count: ',x.count(b'c'))
    print('find: ',x.find(b'c'))
    print('a in x : ', b'a' in x)
    print('x + y : ', x + y)
    print('list(x) : ', list(x))
    print('vals : ', vals)
    print('vals.append(0) vals.append(1) vals.append(2)')
    vals.append(0)
    vals.append(1)
    vals.append(2)
    print('vals : ', vals)
    print('compare, dels, insert can be used like list functions')

if __name__ == "__main__":
    bytes_bytearray()
    bytearray_examples()