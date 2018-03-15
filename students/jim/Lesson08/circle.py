import math

class Circle:

    def __init__(self, rad=1):
        self.rad = float(rad)

    def __str__(self):
        return "circle with radius {:.6f}".format(self.rad)

    def __repr__(self):
        return "Circle({:.6f})".format(self.rad)

    @property
    def diameter(self):
        return self.rad * 2

    @property
    def area(self):
        return math.pi * (self.rad**2)

    @diameter.setter
    def diameter(self, diameter):
        self.rad = diameter/2
        print("diameter is now {}".format(self.diameter))
        print("radius is now {}".format(self.rad))

    def __add__(*args):
        rad_sum = 0
        for arg in args:
            if type(arg) is not Circle:
                raise TypeError("Incompatible operand:", arg)
                break
            else:
                rad_sum += arg.rad
        return Circle(rad_sum)

c1 = Circle(5)
c2 = Circle(3)
