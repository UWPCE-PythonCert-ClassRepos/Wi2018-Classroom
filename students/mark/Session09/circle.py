#!/usr/bin/env python3

#from circle import Circle


import math


class Circle():
    def __init__(self, radius=2):
        self.radius = float(radius)

    @property
    def area(self):
        return math.pi  * self.radius**2

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(int(self.radius))
