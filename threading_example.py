import threading
import time


# Ref 1 : https://niceman.tistory.com/138
# Ref 2 : https://itholic.github.io/python-threading/
def function(num):
    print(threading.current_thread().getName(), num)

    for i in range(5):
        time.sleep(1)
        print(threading.current_thread().getName(),' ', i)

    print(threading.current_thread().getName(),' is finished')

if __name__ == '__main__':
    print('-' * 5 + 'Threading_example' + '-' * 5)
    threading_list = list()
    for i in range(10):
        thread = threading.Thread(target=function, args=(i + 1,))
        thread.start()
        threading_list.append(thread)

    for each_thread in  threading_list:
        each_thread.join()

    print('all threads are finished.')
