#!/usr/bin/env python3


import circle

from circle import Circle # or can do this
### like this class Classname(Circle): 

"""
def test_radius():
    my_circle = Circle(6)
    assert my_circle.radius == 6
"""



class CircleAdd(circle.Circle):
    def __init__(self, radius=2):
        self.radius = float(radius)

    #     #super().__init__(content)
    #
    #
    # def __radd__(self):
    #     self.radius
    #
    def some_output():
        print('some output')




if __name__ == '__main__':
    ac=circle.Circle(5)
    print(ac.area)

    myc=CircleAdd(5)
    print(myc.area)


    #78.53981633974483


    # myc=CircleAdd(2)
    #
    # myc.some_output()
