import math
import functools

@functools.total_ordering
class Circle:
    def __init__(self, radius=0):
        self._radius = radius


    @classmethod
    def from_diameter(myclass, diameter=0):
        return myclass(diameter / 2)


    @property
    def radius(self):
        return self._radius


    @property
    def circumference(self):
        return self._radius * 2 * math.pi


    @property
    def area(self):
        return (self._radius ** 2) * math.pi


    @property
    def diameter(self):
        return self._radius * 2


    @radius.setter
    def radius(self, newradius):
        self._radius = newradius


    @diameter.setter
    def diameter(self, newdiameter):
        self._radius = newdiameter / 2


    def __str__(self):
        return f"Circle with radius: {self._radius:.6f}"


    def __repr__(self):
        return f"Circle({self._radius})"


    def __add__(self, other):
        return Circle(self._radius + other.radius)


    def __mul__(self, other):
        return Circle(self._radius * other)


    def __rmul__(self, other):
        return Circle(self._radius * other)


    def __eq__(self, other):
        return self._radius == other.radius


    def __lt__(self, other):
        return self._radius < other.radius
