#!/usr/bin/env python
from math import pi
# import functools

# Programming in python B Winter 2018
# March 17, 2018
# Circle.py
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom

# this is a trick to make all the greater than, less than, etc work.
# see: https://docs.python.org/3.6/library/functools.html#functools.total_ordering


# @functools.total_ordering
class Circle():
    """
    simple class to represent a Circle
    """

    def __init__(self, radius=4):
        self.radius = float(radius)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2.0)

    @property
    def area(self):
        return pi * self.radius**2

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2.0

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(int(self.radius))

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __imul__(self, factor):
        self.radius *= factor
        return self

    def __rmul__(self, other):
        return Circle(self.radius * other)

# Attempting to follow the use of class sphere
# This is a subclass


class Sphere(Circle):
    def volume(self):
        return 4 / 3 * pi * self.radius ** 3

    def area(self):
        raise NotImplementedError("Spheres don't have an area")

    def __repr__(self):
        return "Sphere({:g})".format(self.radius)

    def __str__(self):
        return "Sphere with radius: {:g}".format(self.radius)
