import math
from functools import total_ordering


@total_ordering
class Circle():
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
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        new_radius = self.radius + other.radius
        return Circle(new_radius)

    def __mul__(self, other):
        if isinstance(other, Circle):
            new_radius = self.radius * other.radius
        else:
            new_radius = self.radius * other
        return Circle(new_radius)

    __rmul__ = __mul__

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):
    def __repr__(self):
        return "Sphere({})".format(self.radius)

    def __str__(self):
        return "Sphere with radius: {:.6f}".format(self.radius)

    @property
    def volume(self):
        return 4 / 3 * math.pi * self.radius**3

    @property
    def surfaceArea(self):
        return 4 * math.pi * self.radius**2
