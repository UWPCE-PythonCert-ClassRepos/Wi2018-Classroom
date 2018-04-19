#!/usr/bin/env python3

"""
http://codingbat.com/prob/p190859

We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.
"""

def make_chocolate(small, big, goal):
    afterbig = (goal - 5 * big)
    if afterbig < 0:
        newbig = goal // 5
        afterbig = goal - 5 * newbig
    if afterbig <= small:
        return afterbig
    return -1
