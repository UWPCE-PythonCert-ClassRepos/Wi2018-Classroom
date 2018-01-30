# Programming in python B Winter 2018
# January 27, 2017
# Fibonacci and Lucas Series
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


#!/usr/bin/env python3

#  This is the fibonacci
def fibonacci(n):
    # TODO: change this description
    """Be sure to update your doc string here"""
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(i) for i in range(1, 11)])


# This is for lucas
def lucas(n):
    # TODO: change this description
    """Be sure to update your doc string here"""
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
    # print(lucas(n))


print([lucas(i) for i in range(1, 11)])
# print(lucas(11))
