
#Ref 1 : https://whatisthenext.tistory.com/112
#Ref 2 : https://nachwon.github.io/closure/
def outer_fucntion(a, b):
  def inner_function(c, d):
    return c + d
  return inner_function(a, b)
# 내부 함수(inner function)은 루프나 코드 중복을 피하기 위해 또 다른 함수 내에 어떤 복잡한 작업을 한 번 이상 수행할 때 유용하게 사용한다.

def outer_func():
    message = 'Hello'
    def inner_func():
        print(message)
    return inner_func # ()를 삭제하여 inner_func를 호출하지 않고 리턴함.

def say_words(msg):
    def say_sentence():
        return "Hello print this!!: {}".format(msg)

    return say_sentence


if __name__ == '__main__':

    print(outer_func()()) # when inner function's return type is None. We can call the function like this.
    print(outer_fucntion(3, 5)) # we can fix closure's variable or

    b = outer_fucntion # we can just pass function name.
    print("b(10,11) : ",b(10,11))
    print("b(5,11) : ",b(5,11))

    a = say_words("Hungry!!")
    print("What is a : ", a)
    print("What is a of type?: ", type(a))
    print("a is an function, run it ====> ", a())
    # 결론 : 클로저는 다른 함수에 의해 동적으로 생성되고, 바깥 함수로부터 생성된 변수값을 알고 있는 변수이다.

    print("dir(a) : ", dir(a))
    print("type(a.__clousre__) : ",type(a.__closure__))
    print("a.__closure__ : ", a.__closure__)
    print("dir(a.__closure__[0]) : ", dir(a.__closure__[0]))
    print("a.__closure__[0].cell_contents : ", a.__closure__[0].cell_contents)
    # 클로저(Closure)를 왜 쓰냐 다시 물어본다면 기존에 만들어진 함수나 모듈 등을 수정하지 않고 wrapper 함수를 이용해서 자기 입맛에 맞게 조정할 수 있다는 것이다.
    """
    Cell Object
   “Cell” objects are used to implement variables referenced by multiple scopes. 
    For each such variable, a cell object is created to store the value; 
    the local variables of each stack frame that references the value contains a reference to the cells from outer scopes which also use that variable.
    from : docs.python.org
    """