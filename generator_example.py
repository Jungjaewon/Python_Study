from __future__ import division
import os
import psutil
import random
import sys
import time
"""
Ref 1: https://bluese05.tistory.com/56
Ref 2: http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A0%9C%EB%84%88%EB%A0%88%EC%9D%B4%ED%84%B0-generator/
Ref 3: https://wikidocs.net/16069

"""

"""
Genrator

A function which returns an iterator. It looks like a normal function except that it contains yield statements for 
producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function. 
Each yield temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements). 
When the generator resumes, it picks-up where it left-off (in contrast to functions which start fresh on every invocation).

yield
The yield statement is only used when defining a generator function, and is only used in the body of the generator function. 
Using a yield statement in a function definition is sufficient to cause that definition to create a generator function instead of a normal function.

When a generator function is called, it returns an iterator known as a generator iterator, or more commonly, 
a generator. The body of the generator function is executed by calling the generator’s next() method repeatedly until it raises an exception.

When a yield statement is executed, the state of the generator is frozen and the value of expression_list is returned to next()‘s caller. 
By “frozen” we mean that all local state is retained, including the current bindings of local variables, 
the instruction pointer, and the internal evaluation stack: enough information is saved so 
that the next time next() is invoked, the function can proceed exactly as if the yield statement were just another external call.

As of Python version 2.5, the yield statement is now allowed in the try clause of a try ... finally construct. 
If the generator is not resumed before it is finalized (by reaching a zero reference count or by being garbage collected), 
the generator-iterator’s close() method will be called, allowing any pending finally clauses to execute.
"""

"""
A generator is memory efficient because each stuff is load when the stuff is required.


"""


def generator(n):
    i = 0
    while i < n:
        yield i
        i += 1


def generator_example():
    print('-' * 5 + 'generator_example' + '-' * 5)
    for x in generator(5):
        print(str(x) + ' ', end='')
    print()


def comprehension_generator():
    print('-' * 5 + 'comprehension_generator' + '-' * 5)
    print('[i for i in range(10) if i % 2] : ', [i for i in range(10) if i % 2])
    print('(i for i in range(10) if i % 2) : ', (i for i in range(10) if i % 2))


def getting_size():
    print('-' * 5 + 'getting_size' + '-' * 5)
    print('sys.getsizeof( [i for i in range(100) if i % 2] ) : ', sys.getsizeof( [i for i in range(100) if i % 2] ))
    print('sys.getsizeof( (i for i in range(100) if i % 2) ) : ', sys.getsizeof( (i for i in range(100) if i % 2) ))
    print('sys.getsizeof( [i for i in range(1000) if i % 2] ) : ', sys.getsizeof([i for i in range(1000) if i % 2]))
    print('sys.getsizeof( (i for i in range(1000) if i % 2) ) : ', sys.getsizeof((i for i in range(1000) if i % 2)))


def sleep_func(x):
    print("sleep... ", end='')
    time.sleep(1)
    return x


def lazy_evlauation():
    print('-' * 5 + 'lazy_evlauation' + '-' * 5)
    print('Using a List')
    input_list = [sleep_func(x) for x in range(5)]
    for i in input_list:
        print(str(i) + ' ', end='')
    print()
    print('Using a Generator')
    gen = (sleep_func(x) for x in range(5))
    for i in gen:
        print(str(i) + ' ', end='')
    print()


def people_list(num_people, names, majors):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people, names, majors):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


def perfomance_test():
    """
    The generator is better than List on memory and speed
    """
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / 1024 / 1024
    names = ['Jack', 'Jake', 'Mark', 'Albe', 'Loni', 'Monte']
    majors = ['CS', 'Korean', 'English', 'Math', 'Politics']

    t1 = time.clock()
    people = people_generator(1000000, names, majors)  # 1 people_generator를 호출
    t2 = time.clock()
    mem_after = process.memory_info().rss / 1024 / 1024 # rss == resident set size
    total_time = t2 - t1
    print('-' * 5 + 'perfomance_test' + '-' * 5)
    print('Generator Example')
    print('Memory Occupancy before: {} MB'.format(mem_before))
    print('Memory Occupancy after: {} MB'.format(mem_after))
    print('Elapsed Time: {:.6f} 초'.format(total_time))

    t1 = time.clock()
    people = people_list(1000000, names, majors)  # 1 people_list를 호출
    t2 = time.clock()
    mem_after = process.memory_info().rss / 1024 / 1024
    total_time = t2 - t1
    print('List Example')
    print('Memory Occupancy before: {} MB'.format(mem_before))
    print('Memory Occupancy after: {} MB'.format(mem_after))
    print('Elapsed Time: {:.6f} 초'.format(total_time))


def test_gen():
    for i in range(10):
        yield i


def same_gen_check():
    """
        a and b are working separately
    """
    print('-' * 5 + 'same_gen_check' + '-' * 5)
    a = test_gen()
    b = test_gen()

    print('a == b : ', a==b)
    print('a is b : ', a is b)

def generator_exception():
    print('-' * 5 + 'generator_exception' + '-' * 5)
    gen = test_gen()

    for i in gen:
        print(str(i) + ' ', end='')
    print()

    # make StopIteration
    for i in range(11):
        print(str(next(gen)) + ' ', end='')
    print()


if __name__ == '__main__':
    generator_example()
    getting_size()
    lazy_evlauation()
    perfomance_test()
    same_gen_check()
    generator_exception()

