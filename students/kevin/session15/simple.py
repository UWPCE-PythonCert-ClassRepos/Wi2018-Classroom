# simple.py
import logging
from logging.handlers import SysLogHandler
from datetime import datetime as dt

format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
format_sans_time = "%(filename)s:%(lineno)-5d %(levelname)s %(message)s"

formatter = logging.Formatter(format)
formatter_sans_time = logging.Formatter(format_sans_time)

file_handler = logging.FileHandler(f'{dt.now():%Y%m%d%H%M%S}.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.NOTSET)
console_handler.setFormatter(formatter)

syslog_handler = SysLogHandler(('0.0.0.0', 514))
syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(formatter_sans_time)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(syslog_handler)

def my_fun(n):
    logging.info(f"Function my_fun called with value {n}")
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error(f"Tried to divide by zero. Var i was {i}. "
                          f"Recovered gracefully.")


if __name__ == "__main__":
    my_fun(100)
