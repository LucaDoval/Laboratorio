import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s - $(threadName)s - %(processName)s - %(levelname)s - %(message)s',
                filename='logger_data.log',
                filemode='a')