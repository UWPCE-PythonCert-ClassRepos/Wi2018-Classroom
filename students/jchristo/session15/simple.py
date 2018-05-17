import logging
import logging.handlers
import datetime


file_and_console_format = '%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s'
syslog_format = '%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s'

file_and_console_formatter = logging.Formatter(file_and_console_format)
syslog_formatter = logging.Formatter(syslog_format, datefmt = '%Y-%m-%d') #define date format as syslog will have its own timestamp

host, port = '0.0.0.0', 514

#for files
file_handler = logging.FileHandler(f'{datetime.datetime.now():%Y-%m-%d}.log') # want these written with current date
file_handler.setLevel(logging.WARNING)           # Warning is fine as we want ALL messages that or higher
file_handler.setFormatter(file_and_console_formatter)

#for console
console_handler = logging.StreamHandler()        # Debug is fine as we want all ALL log messages logged to the console
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(file_and_console_formatter)

#for server
server_handler = logging.handlers.SysLogHandler(host, port)
server_handler.setLevel(logging.ERROR)          # Want ERROR and above
server_handler.setFormatter(syslog_formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)                   # Add this line
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(server_handler)

def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning('The value of i is 50.')
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error(f'Tried to divide by zero. Var i was {i}. Recovered gracefully.')

if __name__ == '__main__':
    my_fun(100)
