#!/usr/bin/env python3

"""
the solution to the generator lab
"""

def intsum():
    """yields sum of ints"""
    tot = 0
    n = 1
    while True:
        yield tot
        tot = tot + n
        n += 1

def intsum2():
    """Someone wrote a test for a second one of these? Y?"""
    tot = 0
    n = 1
    while "arrrrrrr":
        yield tot
        tot = sum([tot,n])
        n += int(True)


def doubler(n=1):
    while True:
        yield n
        n += n


def fib():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime():
    n=3
    yield 2
    while True:
        is_prime = True
        for i in range(2,n//2):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 2  # Cause 2 is only even prime