# simple.py
import logging

format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"

formatter = logging.Formatter(format)

file_handler = logging.FileHandler('mylog.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def my_fun(n):
    logging.info(f"Function my_fun called with value {n}")
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error(f"Tried to divide by zero. Var i was {i}. Recovered gracefully.")

if __name__ == "__main__":
    my_fun(100)
