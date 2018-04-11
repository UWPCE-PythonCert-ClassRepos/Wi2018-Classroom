#!/usr/bin/env python3

"""
https://canvas.uw.edu/courses/1188584/assignments/4189634?module_item_id=8331790
"""

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
    print("Testing iterator 2")
    for i in IterateMe_2():
        print(i)

    it = IterateMe_2(2, 20, 2)
    # These resume where they left off, mostly.  The output skips value 12
    # because we break at that value, then picks up again at 14.
    for i in it:
        if i > 10:  break
        print(i)

    for i in it:
        print(i)


    print("Testing range")
    it = range(2, 20, 2)
    # This restarts at the start of the range
    #  - it appears to be an iterable, not iterator
    for i in it:
        if i > 10:  break
        print(i)

    for i in it:
        print(i)
