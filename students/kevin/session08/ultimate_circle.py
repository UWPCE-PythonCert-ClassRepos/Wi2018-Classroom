#!/usr/bin/env python3
import math


class Circle(object):
    """Documentation for Circle

    """
    def __init__(self, radius=4):
        self.radius = float(radius)

        
    @property
    def area(self):
        return math.pi * self.radius**2

    
    @property
    def diameter(self):
        return 2 * self.radius
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2


    def __str__(self):
        return f'Circle with radius: {self.radius:.6f}'


    def __repr__(self):
        return f'Circle({int(self.radius)})'


    def __add__(self, other):
        self.radius += other.radius
        return self


    def __mul__(self, other):
        self.radius *= other
        return self


    def __rmul__(self, other):
        self.radius *= other
        return self


    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius
