#!/usr/bin/env python3
from circle import *
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
    my_circle = Circle(4)
    assert my_circle.area == math.pi * my_circle.radius ** 2

def test_no_set_area():
    my_circle = Circle(8)
    with pytest.raises(AttributeError):
        my_circle.area = 100

def test_str():
    my_circle = Circle(4)
    assert str(my_circle) == "Circle with radius: 4.000000"

def test_repr():
    my_circle = Circle(4)
    assert repr(my_circle) == 'Circle(4)'

def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert print(c1 + c2) == print(Circle(6))

def test_mul():
    c1 = Circle(2)
    assert print(c1 * 3) == print(Circle(6))

def test_lt_le():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert (c1 > c2) == False
    assert (c1 < c2) == True
    assert (c1 == c2) == False
    assert (c2 <= c3) == True


