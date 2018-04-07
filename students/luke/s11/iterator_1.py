#!/usr/bin/env python3

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
    def __init__(self, start=0, stop=5, step=1):
        self.current = start
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        retval = self.current
        self.current += self.step
        if retval < self.stop:
            return retval
        else:
            raise StopIteration


if __name__ == "__main__":

    print("Testing iterator 1")
    for i in IterateMe_1():
        print(i)

    print("Testing iterator 2")
    for i in IterateMe_2():
        print(i)

    print("Testing iterator 2 non-default parameters")
    for i in IterateMe_2(10, 20, 2):
        print(i)
