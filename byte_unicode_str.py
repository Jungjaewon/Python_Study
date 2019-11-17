import os
from builtins import print

"""
Python3 use bytes, str
a bytes instance has raw 8 bits.
a str instance has unicode character.

Python2 use str, unicode
a str instance has raw 8 bits
unicode instance has unicode character

unicode encoding : UTF-8
Python3 str != Python2 unicode

ascii_code -> unicode
"""

"""
Ref 1 : https://dojang.io/mod/page/view.php?id=2462
Ref 2 : https://excelsior-cjh.tistory.com/117
"""
""" Python3 """


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode('utf-8')
    else:
        return bytes_or_str


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode('utf-8')
    else:
        return bytes_or_str

def casting_example():

    print("-"* 5 + "casting_example" + "-"* 5)
    x = b'bytes_example'
    x = to_str(x)

    if isinstance(x, str):
        print("x is str")
    else:
        print("x is bytes")

    y = 'str_example'
    y = to_bytes(y)

    if isinstance(y, bytes):
        print("y is bytes")
    else:
        print("x is str")

def ascii_code_example():
    print("-" * 5 + "ascii_code_example" + "-" * 5)
    print("ord('a') : ", ord('a')) # return ascii code
    print("ord('b') : ", ord('b')) # return ascii code
    print("ord('c') : ", ord('c')) # return ascii code
    print("ord('0') : ", ord('0')) # return ascii code
    print("ord('1') : ", ord('1')) # return ascii code
    print("ord('2') : ", ord('2')) # return ascii code


def bytes_example():
    print("-" * 5 + "bytes_example" + "-" * 5)
    print("bytes(10) : ", bytes(10))
    print("bytes([10, 20, 30, 40]) : ", bytes([10, 20, 30, 40]))
    print("bytes(b'Hello bytes') : ", bytes(b'Hello bytes'))

def bytearray_example():
    print("-" * 5 + "bytearray_example" + "-" * 5)
    print("bytearray() : ", bytearray())
    print("bytearray(3) : ", bytearray(3))
    print("bytearray([1,2,3,4,5]) : ", bytearray([1,2,3,4,5]))
    print("bytearray(b'Hello bytearray') : ", bytearray(b"Hello bytearray"))


def encoding_decoding_example():
    print("-" * 5 + "encoding_decoding_example" + "-" * 5)
    x = '안녕'.encode('euc-kr')
    y = '안녕'.encode('utf-8')
    print("x = '안녕'.encode('euc-kr')")
    print("y = '안녕'.encode('utf-8')")
    print("'안녕'.encode('euc-kr') : ", '안녕'.encode('euc-kr'))
    print("'안녕'.encode('utf-8') : ",  '안녕'.encode('utf-8'))
    print("x.decode('euc-kr') : ", x.decode('euc-kr'))
    print("y.decode('utf-8') : ", y.decode('utf-8'))

def read_write_example():
    """
    In Python3, 'w' require string with UTF-8
                'wb' require btyes
    :return:
    """
    print("-" * 5 + "read_write_example" + "-" * 5)
    #with open('test.bin','w') as fp:
    with open('test.bin','wb') as fp:
        x = os.urandom(10)
        print("write : x : ",x)
        fp.write(x) # this makes error!! becasue os.urandom(10) makes btyes with the mode 'w'

    with open('test.bin', 'rb') as fp:
        x = fp.read(10)
        print("read : x : ", x)

""" Python2 """
"""
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        return unicode_or_str.decode('utf-8')
    else:
        return unicode_or_str
    
def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        return unicode_or_str.encode('utf-8')
    else:
        return unicode_or_str
"""

if __name__ == "__main__":
    casting_example()
    ascii_code_example()
    bytes_example()
    bytearray_example()
    encoding_decoding_example()
    read_write_example()