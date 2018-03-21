import math
import pytest 

class Circle:
    def __init__(self,radius=2):
        self.radius = float(radius)   #Try c=Circle() & c.radius
    
    @property 
    def area(self):
        return math.pi*self.radius**2   #Try c.area(2)

    @property
    def diameter(self):
        return 2*self.radius   #Try c.diameter(2), Try c.diameter(4)
        
    @diameter.setter  #This sets diameter value to be writable. 
    #Try c.diameter = 8 then try c.radius. 
    def diameter(self, diameter):
        self.radius = diameter/2     

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(int(self.radius))

    def __add__(self,addcircle):
        addedradius = self.radius + addcircle.radius
        return Circle(int(addedradius))

    def __mul__(self,multicircle): 
        multiradius = self.radius*multicircle.radius
        # multiradius = self.radius*multicircle  <-- this is for c1*3. 
        return Circle(int(multiradius))

    def __rmul__(self,anyinteger):  # <-- this if for 3*c1
        multicircle2 = anyinteger*self.radius
        return Circle(int(multicircle2))

    def __eq__(self,equalradi):
        return ((self.radius) == (equalradi.radius))


# Py Tests-------------------------------
#from circle import Circle

def test_radius():
    my_circle = Circle(6)
    assert my_circle.radius == 6

def test_diameter():
    my_circle = Circle(6)
    assert my_circle.diameter == 12

def test_set_diameter():
    my_circle = Circle(4)
    my_circle.diameter = 12
    assert my_circle.radius == 6 
    assert my_circle.diameter == 12

def test_area():
    my_circle = Circle(3)
    assert my_circle.area == math.pi*3**2

def test_no_set_area():
    my_circle = Circle()
    with pytest.raises(AttributeError):
        my_circle.area = 20

def test_str():
    my_circle = Circle(4)
    assert str(my_circle) == "Circle with radius: 4.000000" 

def test_repr():
    my_circle = Circle(4)
    assert repr(my_circle) == 'Circle(4)'   

def test_addCircles():
    my_circle = Circle()
    my_circle1 = Circle(2)
    my_Circle2 = Circle(4)
    assert my_circle1 + my_Circle2 == Circle(6)

def test_multiCircles():
    my_circle = Circle()
    my_circle1 = Circle(2)
    my_circle2 = Circle(4)
    assert my_circle1 * my_circle2 == Circle(8)

def test_integer(): #This test is for testing 'integer x instance'
    my_circle = Circle()
    my_circle1 = Circle(2)
    assert 3*my_circle1 == Circle(6)

def test_speicaloperator():
    my_circle = Circle()
    my_circle1= Circle(2)
    my_circle2 = Circle(4)
    my_circle3 = Circle(4)
    assert my_circle2 == my_circle3
    assert my_circle1 != my_circle2

