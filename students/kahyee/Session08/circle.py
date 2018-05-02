import math

class Circle():
    def __init__(self, radius=4):
        self.radius = float(radius)
    
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
        return "Circle with radius {:6f}" .format(self.radius)
        
    def __repr__(self):
        return "Circle({})" .format(int(self.radius))
        
    def __add__(self, other):
        return Circle(self.radius + other.radius)
        
    def __mul__(self, other):
        return Circle(self.radius * other)
        
    def __rmul__(self, other):
        return Circle(self.radius * other)
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius

class Sphere(Circle):
    
    def __str__(self):
        return "Sphere with radius {:6f}" .format(self.radius)
        
    def __repr__(self):
        return "Sphere({})" .format(int(self.radius))
        
    @property
    def area(self):
        return 4 * math.pi * self.radius ** 2
    
    @property
    def volume(self):
        return 4.0 / 3.0 * math.pi * self.radius ** 3