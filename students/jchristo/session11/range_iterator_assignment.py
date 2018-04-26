#!/usr/bin/env python
import itertools

"""
Simple iterator examples
"""


class IterateMe_1:
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

class IterateMe_2:
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from given start to stop with step
    ( like range(4) )
    """

    def __init__(self, start,stop,step=1):
        self.current = (start - step)
        self.start = start
        self.stop = stop
        self.step = step
        assert (step != 0),"Step must not be zero!"

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            self.current += self.step
            return self.current
        else:
            raise StopIteration

    def __str__(self):
        return int(self.current)

if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe_2(2,20,2):
        print (repr(i))

    print("Testing break point")
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print(i)
    print("Resume after break point")
    for i in it:
        print(i)
