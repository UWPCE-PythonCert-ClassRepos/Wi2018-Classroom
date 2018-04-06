#!/usr/bin/env python
import math

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)
	
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2	
		
    @property
    def area(self):
        return self.radius**2 * math.pi

    @classmethod
    def from_diameter(cls, diameter):
        cls.radius = diameter / 2
        return cls(cls.radius)
		
    def __str__(self):
        return "Circle with radius: {}".format(str(self.radius))	
	
    def __repr__(self):
        return "Circle({})".format(str(self.radius))

    def __add__(self, other):
        return self.radius + other.radius

    def __mul__(self, num):		
        return self.radius * num
		
    def __rmul__(self, num):		
        return self.radius * num		

    def __lt__(self, other): 
        return self.radius < other.radius
    def __le__(self, other):
        return self.radius <= other.radius	
    def __eq__(self, other):
        return (self.radius == other.radius)	
    def __ge__(self, other):
        return self.radius >= other.radius	
    def __gt__(self, other):
        return self.radius > other.radius	
    def __ne__(self, other):
        return self.radius != other.radius	

class Sphere(Circle):
    def __init__(self, radius):    
        Circle.radius = radius
    def __str__(self):
        return "Sphere with radius: {}".format(str(Circle.radius))	
	
    def __repr__(self):
        return "Sphere({})".format(str(Circle.radius))

    @property
    def volume(self):
        return (Circle.radius**3 * math.pi * 4 / 3)        	

    @property
    def area(self):
        return (Circle.radius**2 * math.pi * 4)
		
c = Circle(5)	
c2 =Circle.from_diameter(4)
s = Sphere(5)

sphere_from_diameter = s.from_diameter(10)

if __name__ == '__main__':
    assert c.radius == 5
    assert c.diameter == 10
    c.diameter = 20
    assert c.radius == 10
    assert c.area == 314.1592653589793	
    assert c2.radius == 2.0
    assert c2.area == 12.566370614359172
    assert c.__str__() == 'Circle with radius: 10.0'
    assert c2.__str__() == 'Circle with radius: 2.0'
    assert repr(c) == 'Circle(10.0)'
    assert repr(c2) == 'Circle(2.0)'
    assert c + c2 == 12.0
    assert c * 3 == 30.0
    assert c2 * 3 == 6.0
    assert (c > c2) == True
    assert c * 3 == 3 * c
    assert s.__str__() == 'Sphere with radius: 5.0'
    assert repr(s) == 'Sphere(5.0)'
    assert s.volume == 523.5987755982989
    assert s.area == 314.1592653589793
    assert repr(sphere_from_diameter) == 'Sphere(5.0)'
