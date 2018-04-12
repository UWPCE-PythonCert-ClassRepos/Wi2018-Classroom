#!/usr/bin/env python3

"""
Circle class exercise
"""
import math
from functools import total_ordering


@total_ordering
class Circle:
    def __init__(self, radius=4):
        self.radius = float(radius)

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius**2

    def __repr__(self):
        return f"Circle({str(int(self.radius))})"

    def __str__(self):
        return f"Circle with radius: {self.radius:.6f}"

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    def __add__(self, other):
        return self.radius + other.radius

    def __mul__(self, other):
        if isinstance(other, Circle):
            return self.radius * other.radius
        else:
            return self.radius * other

    # This means that you can multiply either direction. I feel like this
    # should be the default...
    __rmul__ = __mul__

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius



class Sphere(Circle):
    def __repr__(self):
        f"Sphere({str(int(self.radius))})"

    def __str__(self):
        return f"Circle with radius: {self.radius:.6f}"

    @property
    def volume(self):
        return 4/3*pi*self.radius

    @property
    def area(self):
        raise NotImplementedError  # Meh

