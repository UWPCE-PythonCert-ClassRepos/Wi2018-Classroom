#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/fib_and_lucas.html#exercise-fibonacci

Compute Fibonacci sequence.
"""

def fib(n):
    """ Return n-th value in the Fibonacci sequence. """
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return (fib(n - 2) + fib(n - 1))

def lucas(n):
    """ Return the n-th value in the Lucas sequence. """
    if (n == 0):
        return 2
    if (n == 1):
        return 1
    return (lucas(n - 2) + lucas(n - 1))

print("First 10 Fibonacci numbers:")
for i in range(10):
    print(repr(i) + ": " + repr(fib(i)))
print()

print("First 10 Lucas numbers:")
for i in range(10):
    print(repr(i) + ": " + repr(lucas(i)))
