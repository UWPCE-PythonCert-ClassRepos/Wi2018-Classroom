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


if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe_1():
        print(i)


class IterateMe_2:
    """
    New iterator with three input parameters
    """

    def __init__(self, start, stop, step):
        self.current = start
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

    print("Let's test iterator_1")
    for i in IterateMe_1():
        print(i)

    print("Lets test iterator_2")
    it = IterateMe_2(2, 30, 2)
    for i in it:
        if i > 10:
            break
        print(i)

    print("What happens after break? (picks up at 15)")
    for i in it:
        print(i)

    print("I hope this range works")
    print(list([x for x in range(10)]))

    print("IterateMe_2 this is a range")
    print(list(IterateMe_2(-1, 10, 1)))

    print("I'm not clear on the 'is range an iterator or an iteratable?'")
