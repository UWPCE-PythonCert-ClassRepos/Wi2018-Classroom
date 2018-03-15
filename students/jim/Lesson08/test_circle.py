from circle import Circle
import pytest

def test_radius():
    my_circle = Circle(5)
    assert my_circle.rad == 5

def test_str():
    my_circle = Circle(3)
    assert my_circle.__str__() == "circle with radius {:.6f}".format(my_circle.rad)

def test_diameter():
    my_circle = Circle(4)
    assert my_circle.diameter == 8

def test_set_diameter():
    my_circle = Circle(4)
    my_circle.diameter = 12
    assert my_circle.rad == 6

def test_repr():
    my_circle = Circle(4)
    assert my_circle.__repr__() == "Circle({:.6f})".format(my_circle.rad)

def test_compare():
    c1 = Circle(3)
    c2 = Circle(5)
    c3 = Circle(5)
    c4 = Circle(8)
    assert c1 < c2
    assert c2 > c1
    assert c2 == c3
    assert c2 <= c3
    assert c3 >= c2

def test_no_set_diameter():
    c1 = Circle(3)
    with pytest.raises(AttributeError):
        c1.area = 42

def test_add():
    c1 = Circle(4)
    c2 = Circle(8)
    assert c1 + c2 == Circle(12)
    assert c2 + c1 == Circle(12)

def test_multiply():
    my_circle = Circle(7)
    assert my_circle * 3 == Circle(21)
    assert 3 * my_circle == Circle(21)
