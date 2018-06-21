#!/usr/bin/env python3
import math

class Circle:

    def __init__(self, radius=4):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        rad = self.radius + other.radius
        return Circle(rad)

    def __mul__(self, other):
        rad = self.radius * other
        return Circle(rad)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius
