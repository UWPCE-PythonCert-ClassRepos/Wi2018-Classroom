#/usr/bin/env python3

"""
count_evens
prev  |  next  |  chance

Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""

from count_evens import count_evens
# from count_evens import count_evens2 as count_evens
# from count_evens import count_evens3 as count_evens


def test_1():
    assert count_evens([1,2,3]) == 1


def test_2():
    assert count_evens([1,4,6,0]) == 3


def test_3():
    assert count_evens([1,3,5]) == 0


