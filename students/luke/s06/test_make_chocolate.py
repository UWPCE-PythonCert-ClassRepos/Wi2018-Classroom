#!/usr/bin/env python3

"""
Tests for pytest against http://codingbat.com/prob/p190859
"""

import make_chocolate

def test_make_chocolate_1():
    assert make_chocolate.make_chocolate(4, 1, 9) == 4


def test_make_chocolate_2():
    assert make_chocolate.make_chocolate(4, 1, 10) == -1


def test_make_chocolate_2():
    assert make_chocolate.make_chocolate(4, 1, 7) == 2


def test_make_chocolate_2():
    assert make_chocolate.make_chocolate(6, 2, 7) == 2


def test_make_chocolate_2():
    assert make_chocolate.make_chocolate(9, 3, 18) == 3
