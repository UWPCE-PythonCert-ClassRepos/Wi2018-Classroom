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

class Iterator_2(IterateMe_1):

    def __init__(self,start,stop,step=1):
        self.start=start-1
        self.stop=stop
        self.step=step

    def __next__(self):
        self.start += self.step
        if self.start < self.stop:
            return self.start
        else:
            raise StopIteration

if __name__ == "__main__":

    print("Testing the iterator1")
    for i in IterateMe_1():
        print(i)

    print("\n")

    print("Testing the iterator2")
    for i in Iterator_2(0,10,step=2):
        print(i)
