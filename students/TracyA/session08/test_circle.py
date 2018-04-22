#!/usr/bin/env python
from circle import Circle, Sphere
from math import pi
import pytest

# Programming in python B Winter 2018
# March 18  , 2018
# test_circle.py
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


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
    assert my_circle.area == pi * 3**2


def test_no_set_area():
    my_circle = Circle(3)
    with pytest.raises(AttributeError):
        my_circle.area = 20


def test_str():
    my_circle = Circle(4)
    assert str(my_circle) == "Circle with radius: 4.000000"


def test_repr():
    my_circle = Circle(4)
    assert repr(my_circle) == "Circle(4)"


def test_addition():
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 + c2

    assert c3.radius == 5


def test_multiplication():
    c1 = Circle(2)
    c3 = c1 * 4

    assert c3.radius == 8


def test_not_equal():
    c1 = Circle(2.9)
    c2 = Circle(3.0)

    assert c1 != c2


# def test_greater():
#     c1 = Circle(2)
#     c2 = Circle(3)

    # assert c2 > c1
    # assert c2 >= c1


# ####################################
# Test for the Sphere object
# ####################################
def test_sphere_vol():
    s = Sphere(4)

    print(s.volume())
    assert s.volume() == 268.082573106329


def test_sphere_change_radius():
    s = Sphere.from_diameter(8)

    assert s.radius == 4

    s.radius = 3
    assert s.diameter == 6


def test_sphere_diameter():
    s = Sphere.from_diameter(8)

    assert type(s) == Sphere
    print(s.volume())
    assert s.volume() == 268.082573106329
