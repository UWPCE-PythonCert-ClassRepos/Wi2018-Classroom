#!/usr/bin/env python3
"""
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""

from lone_sum import lone_sum as ls

def test_1():
    assert ls(1,2,3) == 6

def test_2():
    assert ls(3,2,3) == 2

def test_3():
    assert ls(3,3,3) == 0

def test_4():
    assert ls(68,233,233)== 68