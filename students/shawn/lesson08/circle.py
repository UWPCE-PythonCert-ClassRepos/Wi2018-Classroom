
import math

class Circle():
    def __init__(self,radius=2):
        self.radius=float(radius)

    @property
    def area(self):
        return math.pi  * self.radius**2

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self,val):
        self.radius=val/2

    def __str__(self):
        return f"Circle with radius: {'{:.4f}'.format(self.radius)}"

    def __repr__(self):
        return f"Circle({int(self.radius)})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return(self.radius,self.diameter) < (other.radius,other.diameter)

    def __eq__(self, other):
        return (self.radius, self.diameter) == (other.radius, other.diameter)

    def __iadd__(self, other):
        return Circle(self.radius + other)

    def __imul__(self, other):
        return Circle(self.radius*other)

    @classmethod
    def from_diameter(cls,val):
        return cls(val/2)

    @staticmethod
    def get_area(radius):
        return Circle(radius).area


class Sphere(Circle):

    def __str__(self):
        return f"Sphere with radius: {'{:.4f}'.format(self.radius)}"

    def __repr__(self):
        return f"Sphere({int(self.radius)})"

    @property
    def volume(self):
        return 4/3 * math.pi * self.radius**3

    @volume.setter
    def volume(self,val):
        self.radius = ((3*val) /(4*math.pi))**(1./3.)
