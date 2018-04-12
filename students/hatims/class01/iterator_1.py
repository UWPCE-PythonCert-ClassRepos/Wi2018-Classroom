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


class IterateMe_2(IterateMe_1):

    def __init__(self, start, stop, step=1):
        self.step = step
        self.cur = start
        super().__init__(stop)		

    def __next__(self):
        self.cur += self.step
        if self.cur < self.stop:
            return self.cur
        else:
            raise StopIteration		

			
if __name__ == "__main__":

    print("Testing the IterateMe_1")
    for i in IterateMe_1():
        print(i)
		
    print("Testing the IterateMe_2")
    for i in IterateMe_2(3, 15, 2):
        print(i)

	