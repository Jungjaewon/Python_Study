import logging
import logging.config
import json
import os

# Ref 1 : https://hamait.tistory.com/880
"""
"loggers": {
"my_module": {
"level": "ERROR",
"handlers": ["console"],
"propagate": "no"
}
},

We can add logger's configuration.

"""
json_config = {
"version": 1,
"formatters": {
"simple": {
"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
}
},

"handlers": {
"console": {
"class": "logging.StreamHandler",
"level": "INFO",
"formatter": "simple",
"stream": "ext://sys.stdout"
},

"info_file_handler": {
"class": "logging.FileHandler",
"level": "DEBUG",
"formatter": "simple",
"filename": "info.log"
}
},

"root": {
"level": "DEBUG",
"handlers": ["console", "info_file_handler"]
}
}

if __name__ == '__main__':
    json_dict = json.dumps(json_config)
    print('json_dict : ', json_dict)
    logging.config.dictConfig(json_config)
    logger = logging.getLogger()
    logger.info("test!!!")

