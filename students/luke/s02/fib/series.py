#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/fib_and_lucas.html#exercise-fibonacci

Compute Fibonacci or Lucas sequence.
"""

def fib(n, n_2=0, n_1=1):
    """ Return n-th value in the Fibonacci/Lucas sequence using supplied terminal values. """
    if (n == 0):
        return n_2
    if (n == 1):
        return n_1
    return (fib(n - 2) + fib(n - 1))

print("First 10 Fibonacci numbers:")
for i in range(10):
    print(repr(i) + ": " + repr(fib(i, 0, 1)))
print()

print("First 10 Lucas numbers:")
for i in range(10):
    print(repr(i) + ": " + repr(fib(i, 2, 1)))
