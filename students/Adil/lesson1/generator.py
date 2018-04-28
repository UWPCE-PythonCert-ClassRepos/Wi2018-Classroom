#!/usr/bin/env python 3
"""
Writing a few generators
"""
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
    last2 = 0
    last1 = 1
    yield 1
    while True:
        val = last2 + last1
        last2 = last1
        last1 = val
        yield val


def prime():
    val = 2 
    while True:
        prime = True
        for i in range(2, val):
            if val % i == 0:  
               prime = False
               break;
        ret = val
        val += 1
        if prime:
            yield ret