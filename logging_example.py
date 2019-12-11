import logging

# Ref 1 : https://hamait.tistory.com/880
# Ref 2 : https://snowdeer.github.io/python/2017/11/17/python-logging-example/
# Ref 3 : https://ourcstory.tistory.com/97
"""
This example is a basic example for logging

"""
if __name__ == '__main__':

    #logging.basicConfig(filename='log_test.log', level=logging.DEBUG)
    # default filemode is a
    """
    Log level
    DEBUG < INFO < WARNING < ERROR < CRITICAL
    """
    logging.debug("Debug")
    logging.info("Info")
    logging.warning("warning")
    logging.error("Error")
    logging.critical("Critical")


