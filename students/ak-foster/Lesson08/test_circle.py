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