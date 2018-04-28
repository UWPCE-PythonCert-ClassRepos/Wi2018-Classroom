#!/usr/bin/env python3

"""
tests for circle_class.py
"""
from circle_class import Circle
import math
import pytest

@pytest.fixture
def my_circle():
    return Circle(4)

def test_radius(my_circle):
    assert my_circle.radius == 4

def test_diameter(my_circle):
    assert my_circle.diameter == 8

def test_set_diameter(my_circle):
    my_circle.diameter = 12
    assert my_circle.radius == 6
    assert my_circle.diameter == 12

def test_area(my_circle):
    assert my_circle.area == math.pi * 4**2

def test_no_set_area(my_circle):
    with pytest.raises(AttributeError):
        my_circle.area = 20

def test_str(my_circle):
    assert str(my_circle) == "Circle with radius: 4.000000"

def test_repr(my_circle):
    assert repr(my_circle) == "Circle(4)"

def test_add(my_circle):
    assert my_circle + my_circle == 8

def test_mutliplication(my_circle):
    assert my_circle * my_circle == 16
    assert my_circle * 2 == 8
    assert 2 * my_circle == 8

def test_gt_lt_eq(my_circle):
    your_circle = Circle(2)
    assert my_circle > your_circle
    assert (my_circle < your_circle) == False
    assert (my_circle == your_circle) == False

def test_sorting(my_circle):
    blah = [Circle(1), Circle(6), Circle(2), Circle(19), Circle(7)]
    assert sorted(blah) == [Circle(1), Circle(2), Circle(6), Circle(7), Circle(19)]

def test_augmented_ass(my_circle):
    my_circle += my_circle
    assert my_circle == 8


