
"""
Ref 1 : https://technote.kr/258
"""
def callable_func():
    print("Callable_function")


class CallableClass(object):

    def __init__(self):
        pass

    def __call__(self, *list_var):
        print("Callable class : ",list_var)


class UncallableClass(object):

    def __init__(self):
        pass

def callable_example():
    print("callable_example")

    class_var = CallableClass()
    unclass_var = UncallableClass()

    print("callable(callable_func) : ", callable(callable_func))
    print("callable(class_var) : ", callable(class_var))
    print("class_var(1,2,3,4,5)", class_var(1, 2, 3, 4, 5))
    print("class_var('hello',' callable')", class_var('hello', ' callable'))
    print("callable(unclass_var) : ", callable(unclass_var))


if __name__ == '__main__':
    callable_example()


