from contextlib import contextmanager

"""
Ref 1 : https://ddanggle.gitbooks.io/interpy-kr/content/ch24-context-manager.html
Ref 2 : https://soooprmx.com/archives/4079

with statement example

"""


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    # without AttributeError: __enter__ is occured
    def __exit__(self, atype, value, trace_back):
        print('atype  : ', str(atype), type(atype), atype)
        print('value  : ', str(value), type(value), value)
        print('trace_back  : ', str(trace_back), type(trace_back), trace_back)
        self.file_obj.close()
        return True # This means exception is treated. if return False, "with" clause makes the exception.
    # without AttributeError: __exit__ is occured

@contextmanager
def open_file(name):
    f = open(name, 'wb')
    yield f # with cluase area yield f is necessary f goes to with cluase
    f.close()

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield  # with cluase area yield  just yield is fine!! 
    print("</%s>" % name)

if __name__ == '__main__':
    """
    with open('some_file', 'w') as opened_file:
        opened_file.write('Hola')
    
    file = open('somefile', 'w')
    try:
        file.write('Hola')
    finally:
        file.close()
    
    Those statement do the same works.
    """
    print('-' * 5 + 'Writing txt files' + '-' * 5)
    with File('demo_binary.txt', 'wb') as opened_file:
        opened_file.write(b'Hello_bin\n')
        opened_file.write(bytes('Hello_bin with bytes\n', encoding='utf-8'))

    with File('demo.txt', 'w') as opened_file:
        opened_file.write('Hello_str\n')

    """
    Generator and Decorator and Context Manager
    """
    print('-' * 5 + 'Generator and Decorator and Context Manager' + '-' * 5)
    print('writing gen_demo.txt')
    with open_file('gen_demo.txt') as f:
        f.write(b'Hola')

    with tag('h1'):
        print("hello")
    """
    Exception Handling
    """
    print('-' * 5 + 'Exception Handling' + '-' * 5)
    with File('demo.txt', 'w') as opened_file:
        opened_file.random_func()




