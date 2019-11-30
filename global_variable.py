
# Ref 1 : https://devbruce.github.io/python/py-13-global,nonlocal/
# Ref 2 : https://rfriend.tistory.com/367

def func():
    global str
    print('str in func : ', str)
    str = 'Python Local Scope'
    print('str in func : ', str)


def f():
    x = 30
    def g():
        x = 60
        def h():
            global x
            x = 120
        h()
    g()


def q():
    x = 40
    def k():
        nonlocal x # nonlocal 이 사용된 함수 ""바로 한단계"" 바깥쪽에 위치한 변수와 바인딩을 할 수 있다.
        x = 80
    k()  # 함수 g를 실행하여 nonlocal이 적용되도록 한다.
    print('x in q : ', x)  # 함수 f에서의 x값이 출력된다.(함수 g에서 nonlocal 의 영향을 받아 변수가 80으로 변경되었다.)

"""
def imposible_example():
    nonlocal x # This statement will occur SyntaxError: no binding for nonlocal 'x' found
    x = 140
"""


def p():
    a = 777
    def g():
        a = 100
        def h():
            global x
            x = 999
            nonlocal a
            a = 333
        h()
        print("[Level 2] a = {}".format(a))
    g()
    print("[Level 1] a = {}".format(a))


if __name__ == '__main__':

    x = 15
    str = 'Python Global Scope'
    func()
    print('str in the main : ', str)
    print('-' * 5 + 'Example 1' + '-' * 5)
    f()
    print('x in the main : ', x)
    print('-' * 5 + 'Example 2' + '-' * 5)
    q()
    print('x in the main : ', x)
    print('-' * 5 + 'Example 3' + '-' * 5)
    p()
    print('x in the main : ', x)