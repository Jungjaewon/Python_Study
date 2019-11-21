"""

None is evaluated to False.
Then, function should not return None
Than should raise exception in the function.
None makes code ambiguous

"""

def func(a,b):

    try:
        c = a / b
        return c
    except ZeroDivisionError as e:
        print("msg : ", e)
        print("Please check the input value")
        return -1

if __name__ == '__main__':

    flag1 = None
    flag2 = False

    print('flag1 : ',flag1)
    print('flag2 : ',flag2)
    print('not flag1 : ', not flag1)
    print('not flag2 : ', not flag2)

    print('func(3,4) : ', func(3,4))
    print('func(3,4) : ', func(1,4))
    print('func(0,3) : ', func(0,3))
    print('func(2,0) : ', func(2,0))


