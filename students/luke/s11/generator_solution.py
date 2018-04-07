#!/usr/bin/env python3

"""
https://canvas.uw.edu/courses/1188584/assignments/4189634?module_item_id=8331790"""

def intsum():
    val = 0
    sum = 0
    while True:
        sum += val
        val += 1
        yield sum

def intsum2():
    return intsum()


def doubler():
    val = 1
    while True:
        yield val
        val *= 2


def fib():
    """ This should start at 0 instead of 1 """
    last2 = 0
    last1 = 1
    yield 1
    while True:
        val = last2 + last1
        last2 = last1
        last1 = val
        yield val


def prime():
    val = 2 # First prime
    while True:
        prime = True
        for i in range(2, val):
            if val % i == 0:  # Not prime
                prime = False
                break;
        ret = val
        val += 1
        if prime:
            yield ret

