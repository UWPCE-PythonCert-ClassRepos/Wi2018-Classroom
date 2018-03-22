import math

class Circle():
    def __init__(self, radius=2.0):
        self.radius = float(radius)

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter/2)
        return self

    @property
    def area(self):
        return math.pi + self.radius**2

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    @property
    def diameter(self):
        return self.radius*2
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2

    def __str__(self):
        return "Circle: (radius: {:f}, diameter: {:f}, circumference: {:f}, area: {:f})".format(self.radius, self.diameter, self.circumference, self.area)

    def __repr__(self):
        return "Circle({:f})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

if __name__ == "__main__":
    print("creating circle with radius 4...")
    d1 = Circle(4)
    print("d1 = ", d1)

    print("changing original diameter to 20...")
    d1.diameter = 20
    print("d1 = ", d1)

    print("creating new circle from diameter of 40...")
    d1 = Circle.from_diameter(40)
    print("d1 = ", d1)

    c1 = Circle(2)
    print("c1 = ", c1)
    c2 = Circle(2) + Circle(3)
    print("c2 = ", c2)
    c3 = Circle(3) * 2
    print("c3 = ", c3)


    print("c1 > c2:  ", c1 > c2)
    print("c1 < c2:  ", c1 < c2)
    print("c1 == c2: ", c1 == c2)