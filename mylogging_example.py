import logging

# Ref 1 :  https://hamait.tistory.com/880

if __name__ == '__main__':
    # logging.getLogger() # root logger is returned.
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    mylogger.addHandler(stream_hander)

    file_handler = logging.FileHandler('my.log') # my.log is a filename
    mylogger.addHandler(file_handler)

    mylogger.debug("server start!!!")
    mylogger.info("server start!!!")
    mylogger.fatal("server start!!!")

