#!/usr/bin/env python3

"""
https://canvas.uw.edu/courses/1188584/assignments/4189639?module_item_id=8331807

Write a recursive.py solution for the factorial function.
"""


def fact(n):
    if n < 1: raise ValueError
    if n == 1: return 1
    return n * fact(n-1)

if __name__ == "__main__":
    assert(fact(10) == 3628800)
