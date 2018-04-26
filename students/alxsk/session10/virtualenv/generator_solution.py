#!/usr/bin/env python

'''Generators'''

import math

def intsum():
    i = 0
    yield intsum(i)
    i += 1

def intsum2():
    pass

def doubler(x):
    x = x
    while True:
        yield x*2
        x = x*2

def fib():
    i = 0
    while True:
        yield fib(i)
        i += 1

#Prime number generator
def is_prime(n):
    for i in xrange(2, 1 + int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def prime():
    yield 2
    for p in itertools.count(3, 2):
        if is_prime(p):
            yield p        

