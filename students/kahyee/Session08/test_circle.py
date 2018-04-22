from circle import Circle, Sphere
import math
import pytest


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
    my_sphere = Sphere(3)
    assert my_circle.area == math.pi * 9
    assert my_sphere.area == 4 * math.pi * 9
    
def test_no_set_area():
    my_circle = Circle()
    with pytest.raises(AttributeError):
        my_circle.area = 4
        
def test_str():
    my_circle = Circle(4)
    my_sphere = Sphere(4)
    assert str(my_circle) == "Circle with radius 4.000000"
    assert str(my_sphere) == "Sphere with radius 4.000000"
    
def test_repr():
    my_circle = Circle(4)
    my_sphere = Sphere(4)
    assert repr(my_circle) == "Circle(4)"
    assert repr(my_sphere) == "Sphere(4)"
    
def test_add():
    assert repr(Circle(4) + Circle(4)) == "Circle(8)"
    
def test_mult():
    assert repr(Circle(4) * 3) == "Circle(12)"
    assert repr(3 * Circle(4)) == "Circle(12)"
    
def test_comparisons():
    assert Circle(4) < Circle(5)
    assert not(Circle(4) < Circle(3))
    assert Circle(4) == Circle(4)
    assert not(Circle(4) == Circle(5))
    assert Circle(5) > Circle(4)
    assert not(Circle(4) > Circle(5))
    
def test_sort():
    circle_list = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circle_list.sort()
    assert circle_list == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

def test_volume():
    my_sphere = Sphere()
    assert my_sphere.volume == 4 / 3 * my_sphere.radius ** 3  * math.pi


    
    