#!/usr/bin/python3
from ultimate_circle import Circle
import math
import pytest


@pytest.fixture
def my_circle():
    return Circle(4)


def test_radius():
    assert my_circle.radius == 4


def test_diameter():
    assert my_circle.diameter == 8

   
def test_set_diameter():
    my_circle.diameter = 12
    assert my_circle.radius == 6
    assert my_circle.diameter == 12


def test_area():
    assert my_circle.area == math.pi * 4**2


def test_no_set_area():
    with pytest.raises(AttributeError):
        my_circle.area = 20


def test_str():
    assert str(my_circle) == "Circle with radius: 4.000000"


def test_repr():
    assert repr(my_circle) == 'Circle(4)'


def test_add():
    
