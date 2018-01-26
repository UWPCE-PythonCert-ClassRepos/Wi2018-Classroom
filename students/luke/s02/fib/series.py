#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/fib_and_lucas.html#exercise-fibonacci

Compute Fibonacci or Lucas sequence.
"""

def series(n, n_2=0, n_1=1):
    """ Return n-th value in the Fibonacci/Lucas sequence using supplied terminal values. """
    if (n == 0):
        return n_2
    if (n == 1):
        return n_1
    return (series(n - 2, n_2, n_1) + series(n - 1, n_2, n_1))

# Test Fibonacci sequence
assert(series(5) == 5)
assert(series(9) == 34)
print("Passed Fibonacci sequence tests.")

# Test Lucas Sequence
assert(series(5, 2, 1) == 11)
assert(series(7, 2, 1) == 29)
print("Passed Lucas sequence tests.")

# Test defaults
assert(series(25) == series(25, 0, 1))
print("Passed default value tests.")
