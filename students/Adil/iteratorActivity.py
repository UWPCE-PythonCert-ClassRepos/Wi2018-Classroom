#usr/bin/env python3

"""
returns the sequence of the numbers from zero to 4

"""
class IterateMe_1:

    def __init__(self, stop=5):
        self.current = 0
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.stop:
            self.current += 1
            return self.current
        else:
            raise StopIteration

class IterateMe_2:

    def _init_(self, start=0, stop=5, step=1):
        self.current = start
        self.start =start
        self.stop = stop
        self.step = step

    def __iter__(self):
            return self

    def __next__(self):
        returnval = self.current
        self.current += self.self
        if returnval < self.stop:
            return returnval
        else:
            raise StopIteration

    def frange(start, stop, step):
        i = start
        while i < stop:
            yield i
            i += stop
    for i in frange(0,5,1):
        print(i)




