import logging
from logging import handlers

class Logger():
    def my_log(self):
        mylog=logging.getLogger("log")
        mylog.setLevel(level=logging.INFO)
        sh=logging.StreamHandler()
        fh=logging.FileHandler(filename="../Log/log.txt",encoding="utf-8")
        fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
        datefmt = "%a %d %b %Y %H:%M:%S"
        formatter = logging.Formatter(fmt, datefmt)
        fh.setFormatter(formatter)
        mylog.addHandler(sh)
        mylog.addHandler(fh)
        return mylog


if __name__ == '__main__':
    log = Logger().my_log()
    # print(log)
    log.info("abc")
