"""
Ref 1 : http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-oop-part-6-%EB%A7%A4%EC%A7%81-%EB%A9%94%EC%86%8C%EB%93%9C-magic-method/
Ref 2 : https://corikachu.github.io/articles/python/python-magic-method
Ref 3 : https://ziwon.dev/post/python_magic_methods/
Ref 4 : https://niceman.tistory.com/196

"""
"""
magic method supports operator over_roding such as add, sub, comparative, bit, casting
magic method has constructor, distructor, new


__enter__
__exit__
enter and exit is used for 'with'


__getinitargs__(self)
__getnewargs__(self)
__getstate__(self)
__setstate__(self, state)
__dict__
__reduce__(self)
__reduce_ex__(self)
__reduce__
These magic methods are used with pickle.

dir shows all magic methods.

"""

class Example(object):

    def __init__(self):
        pass
    def __repr__(self):
        pass
    def __str__(self):
        pass
    def __add__(self, other):
        pass
    def __sub__(self, other):
        pass
    def __lt__(self, other):
        pass
    def __gt__(self, other):
        pass

class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return 'Student Class Info : {} , {}'.format(self._name, self._height)

    def __ge__(self, x):
        print('Called. >> __ge__ Method.')
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x):
        print('Called. >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):
        print('Called. >> __sub__ Method.')
        return self._height - x._height


def magic_method_int():
    print('-' * 5 + 'magic_method_int' + '-' * 5)
    # 기본형
    print(int)

    # 모든 속성 및 메소드 출력
    print(dir(int))
    print()

    n = 100

    # 사용
    print('EX1-1 - n + 200 : ', n + 200)
    print('EX1-2 - n.__add__(500) : ', n.__add__(500))
    print('EX1-3 - n.__doc__ : ', n.__doc__)
    print('EX1-4 - n.__bool__() : ', n.__bool__())
    print('EX1-5 - n.__mul__(100) : ', n.__mul__(100))

def magic_method_class():
    print('-' * 5 + 'magic_method_class' + '-' * 5)
    print(Student)
    print(dir(Student))
    s1 = Student('James', 181)
    s2 = Student('Mie', 165)

    # 매직메소드 출력
    print('EX2-1 - s1 >= s2 : ', s1 >= s2)
    print('EX2-2 - s1 <= s2 : ', s1 <= s2)
    print('EX2-3 - s1 - s2 : ', s1 - s2)
    print('EX2-4 - s2 - s1 : ', s2 - s1)
    print('EX2-5 - s1 : ', s1)
    print('EX2-6 - s2 : ', s2)

if __name__ == '__main__':
    magic_method_int()
    magic_method_class()


