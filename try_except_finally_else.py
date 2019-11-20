"""
Ref 1 : https://wayhome25.github.io/python/2017/02/26/py-12-exception/
Ref 2 : https://gomguard.tistory.com/122
Ref 3 : https://docs.python.org/ko/3/tutorial/errors.html
Ref 4 : http://blog.naver.com/PostView.nhn?blogId=baekmg1988&logNo=220943831113

"""


def try_except_else_example():
    print('-' * 5 + 'try_except_else_example' + '-' * 5)
    try:
        a = [1, 2, 3]
        print('a[4] : ',a[4])
        print('b : ', b)
    except IndexError as e:
        print(e)
        print("Index error is happened")
    except NameError as e:
        print(e)
        print("Name error is happened")


def try_except_pass_example():
    print('-' * 5 + 'try_except_pass_example' + '-' * 5)
    try:
        a = [1, 2, 3]
        print('a[4] : ',a[4])
    except IndexError as e:
        print("Pass the line")


class CustomException(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def Custom_raise_exception():
    print('-' * 5 + 'Custom_raise_exception' + '-' * 5)
    raise CustomException('Custom Exeption')
    #raise CustomException('Custom Exeption')
    # both lines are fine


def try_except_else():
    print('-' * 5 + 'try_except_else' + '-' * 5)
    try:
        print("Get!!")
    except:
        print("Failed")
    else: # This state is excuted when try is success
        print("Try is passed")

def try_except_else_finally():
    print('-' * 5 + 'try_except_else_finally' + '-' * 5)
    try:
        print("Get!!")
    except:
        print("Failed")
    else: # This state is excuted when try is success
        print("Try is passed")
    finally:
        print("must be processed")

def rasie_exception():
    print('-' * 5 + 'rasie_exception' + '-' * 5)
    raise NotImplementedError


if __name__ == '__main__':
    try_except_else_example()
    try_except_pass_example()
    try_except_else()
    try_except_else_finally()
    rasie_exception()
    Custom_raise_exception()

