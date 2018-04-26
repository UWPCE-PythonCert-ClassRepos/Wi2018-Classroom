#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1:
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, start=0, stop=5, step=1):
        self.current = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration



if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe_1():
        print(i)
    print("Testing advanced iterator")
    it = IterateMe_1(2, 20, 2)
    for i in it:
        if i > 10:
            print(i)
            break
        print(i)
    for i in it:
        print(i)

