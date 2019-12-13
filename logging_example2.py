import logging

# Ref 1 : https://hamait.tistory.com/880
# default logging level is warning
"""
logger scope
1. module
2. instance
3. class
4. function

This example makes two loggers in main module.
I do not know how they have the connection.
"""

if __name__ == '__main__':
    # 루트 로거 생성
    rootlogger = logging.getLogger()
    rootlogger.setLevel(logging.INFO)
    stream_hander = logging.StreamHandler()
    rootlogger.addHandler(stream_hander)
    rootlogger.info("root logger message!!")
    # "my" 로거 생성
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.INFO)
    stream_hander2 = logging.StreamHandler()
    mylogger.addHandler(stream_hander2)
    # mylogger.propagate = 0
    # "my" 로거 생성
    mylogger.info("message from mylogger")

