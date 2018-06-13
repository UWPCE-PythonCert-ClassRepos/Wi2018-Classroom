#!/usr/bin/env python

import logging
import logging.handlers
import datetime as dt
import syslogserver as syslog
import socketserver

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

formatter = logging.Formatter(format)
today_date = dt.date.today()
file_handler = logging.FileHandler(str(today_date) + '.log')
file_handler.setLevel(logging.WARNING)           
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()        
console_handler.setLevel(logging.DEBUG)          
console_handler.setFormatter(formatter)          

syslog_handler = logging.handlers.SysLogHandler(address=("localhost", 514))
syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)                   
logger.addHandler(file_handler)
logger.addHandler(console_handler)    
logger.addHandler(syslog_handler)           

def my_fun(n):
    for i in range(0, n):
        logger.debug(i)
        if i == 50:
            logger.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logger.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

if __name__ == "__main__":
    my_fun(100)