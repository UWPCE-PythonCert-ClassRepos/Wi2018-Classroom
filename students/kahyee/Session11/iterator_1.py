#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1:
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers with a user defined start and stop point and step behavior. Behaves like the range function.
    """

    def __init__(self, start, stop, step=1):
        self.current = start - step
        self.start = start
        self.step = step
        self.stop = stop

    def __iter__(self):
        self.current = self.start - self.step
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print("Testing the iterator")
    it = IterateMe_1(2, 20, 2)
    for i in it:
        if i > 10:  break
        print(i)
    for i in it:
        print(i)
        
"""
Initially does not match range behavior because the object keeps it's state after breaking from the loop. (initial code below)

class IterateMe_1:

    About as simple an iterator as you can get:

    returns the sequence of numbers with a user defined start and stop point and step behavior. Behaves like the range function.

    def __init__(self, start, stop, step=1):
        self.current = start - step
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration
"""
