#!/usr/bin/env python3

import datetime
import logging
import logging.handlers

"""
https://canvas.uw.edu/courses/1188584/assignments/4192824?module_item_id=8336635
"""

dflformat = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
formatter = logging.Formatter(dflformat)

logfile = str(datetime.date.today()) + '.log'
file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.WARNING)           
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()        
console_handler.setLevel(logging.DEBUG)          
console_handler.setFormatter(formatter)          

syslogformat = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"
syslogformatter = logging.Formatter(syslogformat)

syslog_handler = logging.handlers.SysLogHandler(address=('syslog', 514))
syslog_handler.setLevel(logging.ERROR)          
syslog_handler.setFormatter(syslogformatter)          

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)                   
logger.addHandler(file_handler)
logger.addHandler(console_handler)               
logger.addHandler(syslog_handler)               

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
