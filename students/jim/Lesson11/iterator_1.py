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

    def __init__(self, start=-1, stop=5, step=1):
        self.current, self.start = start, start
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

    def reset(self):
        self.current = self.start


if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe_1(-1, 50, 4):
        print(i)

    it = IterateMe_1(2, 20, 2)

    for i in it:
        if i > 10:
            it.reset()
            break
        print(i)

    for i in it:
        print(i)
