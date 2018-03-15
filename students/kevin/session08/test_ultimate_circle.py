#!/usr/bin/python3
from ultimate_circle import Circle
import math
import pytest


@pytest.fixture
def my_circle():
    return Circle(4)
@pytest.fixture
def my_circle2():
    return Circle(6)


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
    assert repr(my_circle) == 'Circle(4)'


def test_add(my_circle, my_circle2):
    assert repr(my_circle + my_circle2) == 'Circle(10)'


def test_mult(my_circle):
    assert repr(my_circle * 3) == 'Circle(12)'


def test_rmult(my_circle):
    assert repr(3 * my_circle) == 'Circle(12)'


def test_lt(my_circle, my_circle2):
    assert repr(my_circle < my_circle2) == 'True'
    assert repr(my_circle2 < my_circle) == 'False'


def test_gt(my_circle, my_circle2):
    assert repr(my_circle > my_circle2) == 'False'
    assert repr(my_circle2 > my_circle) == 'True'


def test_eq(my_circle, my_circle2):
    c3 = Circle(4)
    assert repr(my_circle == my_circle2) == 'False'
    assert repr(my_circle == c3) == 'True'
