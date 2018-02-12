#!/usr/bin/env python
# Programming in python B Winter 2018
# January 27, 2017
# Fibonacci and Lucas Series
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


# This is the fibonacci
def fibonacci(n):
    # TODO: change this description
    """This function will print a fibonacci sequence of number"""
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print([fibonacci(i) for i in range(1, 11)])


# This is for lucas
def lucas(n):
    """This function will print a lucas sequence of numbers"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


print([lucas(i) for i in range(1, 11)])


# This is the series
def sum_series(n, a=0, b=1):
    """This function will print a Sum  sequence of numbers"""
    if n == 0:
        return 0
    if n == 1:
        return a
    if n == 2:
        return b
    else:
        return sum_series(n - 2, a, b) + sum_series(n - 1, a, b)


print(sum_series(10))
print(sum_series(10, 2, 1))
