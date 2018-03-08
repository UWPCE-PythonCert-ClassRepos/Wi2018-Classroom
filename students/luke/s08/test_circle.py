#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/circle_class.html#exercise-circle-class
"""
import circle
import pytest


def test_radius():
    myc = circle.Circle(2)
    assert myc.radius == 2


def test_circumference():
    myc = circle.Circle(2)
    assert myc.circumference == 12.566370614359172


def test_area():
    myc = circle.Circle(2)
    assert myc.area == 12.566370614359172


def test_diameter():
    myc = circle.Circle(2)
    assert myc.diameter == 4


def test_setter():
    myc = circle.Circle(2)
    assert myc.diameter == 4
    myc.diameter = 8
    assert myc.radius  == 4


def test_badsetter():
    myc = circle.Circle(2)
    with pytest.raises(AttributeError):
        myc.area = 10


def test_str():
    myc = circle.Circle(4)
    assert str(myc) == "Circle with radius: 4.000000"


def test_repr():
    myc = circle.Circle(4)
    # Use eval(repr(myc)) == something?
    #assert myc == "Circle(4)"
    assert repr(myc) == "Circle(4)"


def test_add():
    myc1 = circle.Circle(4)
    myc2 = circle.Circle(4)
    assert repr(myc1 + myc2) == repr(circle.Circle(8))
