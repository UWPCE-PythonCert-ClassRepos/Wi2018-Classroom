import logging
import logging.handlers
import socket
import sys
from syslogserver import *

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
format2 = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"

formatter = logging.Formatter(format)
formatter2 = logging.Formatter(format2)

file_handler = logging.FileHandler('mylog.log')
file_handler.setLevel(logging.WARNING)           
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()        
console_handler.setLevel(logging.DEBUG)          
console_handler.setFormatter(formatter)

error_handler = logging.handlers.SysLogHandler(address = ('0.0.0.0', 514))
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter2)          

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