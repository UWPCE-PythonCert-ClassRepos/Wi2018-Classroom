# Run me in pytest

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


def test_eq():
    myc1 = circle.Circle(4)
    myc2 = circle.Circle(4)
    assert myc1 == myc2


def test_lt():
    myc1 = circle.Circle(2)
    myc2 = circle.Circle(4)
    assert myc1 < myc2
    assert not myc1 > myc2
    assert not myc1 >= myc2
    assert not myc1 == myc2


def test_diameter_constructor():
    myc1 = circle.Circle.from_diameter(4)
    assert myc1.radius == 2


def test_lt():
    myc1 = circle.Circle(10)
    myc2 = circle.Circle(5)

    circles = [myc1, myc2]
    circles.sort()

    assert(circles == [myc2, myc1])


def test_mul():
    myc1 = circle.Circle(4)
    myc2 = myc1 * 3
    assert myc2 == circle.Circle(12)
    assert myc2 == 3 * myc1
