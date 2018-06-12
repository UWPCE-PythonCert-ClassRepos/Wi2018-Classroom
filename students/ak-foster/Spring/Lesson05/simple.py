#!/usr/bin/env python3

import datetime
import logging
from logging.handlers import SysLogHandler

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

formatter = logging.Formatter(format)

file_handler = logging.FileHandler(f'{datetime.date.today()}.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

sys_handler = logging.handlers.SysLogHandler()
sys_handler.setLevel(logging.ERROR)
sys_handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)-3d %(levelname)s %(message)s"))

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

if __name__ == "__main__":
    my_fun(100)