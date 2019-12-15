# Ref 1 : https://hamait.tistory.com/752
"""
This example is about making threads using class inheritance.

"""
import threading
import time


loops = [8,2]


class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self,name=name)
        self.func = func
        self.args = args

    def run (self):
        self.func(*self.args)
        # 함수를 받아서 처리하는게 아니라 여기에 직접 구현하는 경우가 일반적..


def loop(nloop, nsec):
    print('start loop', nloop, 'at:',time.ctime())
    time.sleep(nsec)
    print('loop', nloop, 'at:', time.ctime())


def test() :
    print('starting at:', time.ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i,loops[i]),loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all Done at: ', time.ctime())


if __name__ == '__main__' :
    test()





