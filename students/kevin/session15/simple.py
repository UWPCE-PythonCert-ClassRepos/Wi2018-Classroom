# simple.py
import logging

format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
logging.basicConfig(level=logging.WARNING, format=format, filename='mylog.log')

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
