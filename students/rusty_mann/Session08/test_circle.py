from circle import Circle
import pytest
import math

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
    assert my_circle.area == math.pi * 3**2

def test_no_set_area():
    my_circle = Circle(3)
    with pytest.raises(AttributeError):
        my_circle.area = 20

def test_str():
    my_circle = Circle(4)  #should be using fixture to not keep repeating this line
    assert str(my_circle) == "Circle with radius: 4.000000"

def test_repr():
    my_circle = Circle(4)
    assert repr(my_circle) == "Circle(4.0)"

def test_add_circles():
    c1 = Circle(4)
    c2 = Circle(3)
    assert c3.radius == 7

