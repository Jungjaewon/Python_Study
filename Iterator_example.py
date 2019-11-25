
"""
Ref 1 : https://nvie.com/posts/iterators-vs-generators/
Ref 2 : https://bluese05.tistory.com/55
Ref 3 : https://kkamikoon.tistory.com/91

"""

if __name__ == '__main__':
    set_a = set([1,2,3,4,5])
    list_a = list([1,2,3,4,5])
    str_a = 'example'

    print('type(set_a) : ', type(iter(set_a)))
    print('type(list_a) : ', type(iter(list_a)))
    print('type(str_a) : ', type(iter(str_a)))
    print('type(iter(set_a)) : ', type(iter(set_a)))
    print('type(iter(list_a)) : ', type(iter(list_a)))
    print('type(iter(str_a)) : ', type(iter(str_a)))
    print('type(iter(iter(set_a))) : ', type(iter(iter(set_a))))
    print('type(iter(iter(list_a))) : ', type(iter(iter(list_a))))
    print('type(iter(iter(str_a))) : ', type(iter(iter(str_a))))

    for x in iter(str_a):
        print(x)

