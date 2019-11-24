import itertools
from itertools import count
from itertools import islice
from itertools import tee
from itertools import repeat
from itertools import cycle
"""
Ref 1 : https://hamait.tistory.com/803
Ref 2 : https://suwoni-codelab.com/python%20%EA%B8%B0%EB%B3%B8/2018/03/07/Python-Basic-itertools/
Ref 3 : https://itholic.github.io/python-combination-permutation/

itertools provide useful functions.
"""


def chaining_example():
    """
    + operator can be used instead of the function.
    """
    print('-' * 5 + 'chaining_example' + '-' * 5)
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    booleans = [1, 0, 1, 0, 0, 1]
    decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

    print(list(itertools.chain(letters, booleans, decimals)))

def counting_example():
    print('-' * 5 + 'counting_example' + '-' * 5)
    """
    in Python3, izip is unresolved.
    count(start,[step])
    """
    for number, letter in zip(count(0, 10), ['a', 'b', 'c', 'd', 'e']):
        print('{0}: {1}'.format(number, letter))


def slicing_example():
    print('-' * 5 + 'slicing_example' + '-' * 5)
    """
    islice(iterable, [start],end,[step])
    """
    for i in islice(range(10), 5):
        print(i, end=' ')
    print()

def tee_example():
    print('-' * 5 + 'tee_example' + '-' * 5)
    i1, i2, i3 = tee(range(7), 3)
    print('i1 : ', i1)
    print('i2 : ', i2)
    print('i3 : ', i3)
    """
    i1, i2, i3 are generators.
    """
    print('list(i1) : ', list(i1))
    print('list(i1) : ', list(i1))
    print('list(i2) : ', list(i2))
    print('list(i2) : ', list(i2))
    print('list(i3) : ', list(i3))
    print('list(i3) : ', list(i3))


def repeat_example():
    print('-' * 5 + 'repeat_example' + '-' * 5)
    print(list(repeat('Hello, world!', 3)))


def cycle_example():
    print('-' * 5 + 'cycle_example' + '-' * 5)
    """
    count(start_num, step)
    """
    for number, letter in zip(cycle(range(2)), ['a', 'b', 'c', 'd', 'e']):
        print('{0}: {1}'.format(number, letter))

def filtering_example():
    print('-' * 5 + 'filtering_example' + '-' * 5)
    from itertools import dropwhile
    print('lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1]))')
    print('dropwhile : ',list(dropwhile(lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1])))
    from itertools import takewhile
    print('takewhile : ',list(takewhile(lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1])))

def groupby_example():
    print('-' * 5 + 'groupby_example' + '-' * 5)

    from operator import itemgetter
    from itertools import groupby
    from collections import defaultdict


    attempts = [
        ('dan', 87),
        ('erik', 95),
        ('jason', 79),
        ('erik', 97),
        ('dan', 100)
    ]

    # Sort the list by name for groupby
    attempts.sort(key=itemgetter(0))
    print('attempts.sort : ',attempts)
    """
    What is an itemgetter?
    """
    # Create a dictionary such that name: scores_list
    # map(func, iterable)

    print('for key, value in groupby(attempts, key=itemgetter(0))')
    for key, value in groupby(attempts, key=itemgetter(0)):
        print('key : ', key)
        print('value : ', list(value))

    print()
    print({key: sorted(map(itemgetter(1), value)) for key, value in groupby(attempts, key=itemgetter(0))})

    counts = defaultdict(list)
    attempts = [('dan', 87), ('erik', 95), ('jason', 79), ('erik', 97), ('dan', 100)]

    for (name, score) in attempts:
        counts[name].append(score)

    print('counts : ', counts)

def permutations_combination_example():
    pool = ['A', 'B', 'C']
    print('-' * 5 + 'permutations_combination_example' + '-' * 5)
    print('pool = ["A", "B", "C"]')
    print('3P3 : ', list(map(''.join, itertools.permutations(pool))))  # 3개의 원소로 수열 만들기
    print('3P2 : ',list(map(''.join, itertools.permutations(pool, 2))))  # 2개의 원소로 수열 만들기

    print('combinations!!')
    print('3C2 : ', list(map(''.join, itertools.combinations(pool, 2))))
    print('3C3 : ', list(map(''.join, itertools.combinations(pool, 3))))


if __name__ == '__main__':
    chaining_example()
    counting_example()
    slicing_example()
    tee_example()
    repeat_example()
    cycle_example()
    filtering_example()
    groupby_example()
    permutations_combination_example()



