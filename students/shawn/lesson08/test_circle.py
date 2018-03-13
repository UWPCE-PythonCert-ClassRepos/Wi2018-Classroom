from circle import Circle
import math
import  pytest
import random as r

@pytest.fixture
def data():
	return Circle(6)

def test_radius():
    assert data().radius==6


def test_diameter():
    assert data().diameter == 12

def test_set_diameter():
    c = Circle(4)
    c.diameter=12
    assert c.radius == 6
    assert c.diameter==12

def test_area():
    c=Circle(1)
    assert data().area==math.pi * 6**2

def test_area_setter():
    with pytest.raises(AttributeError):
        data().area=10

def test_str():
    assert str(data())=="Circle with radius: 6.0000"

def test_repr():
    assert repr(data()) == "Circle(6)"

def test_add():
    c=data()+data()
    assert c.radius==12

def test_mul():
    assert (data()*2).radius==12
    assert (2*data()).radius==12

def test_sort():
    slist=sorted([Circle(5),Circle(3),Circle(1)])
    assert slist[0] == Circle(1)
    assert slist[1] == Circle(3)
    assert slist[2] == Circle(5)

def test_sort_fail():
    with pytest.raises(AssertionError) as e:
        slist = sorted([Circle(5), Circle(3), Circle(1)])
        assert slist[0] == Circle(5)
        assert slist[1] == Circle(3)
        assert slist[2] == Circle(1)

def test_aug_add():
    c=Circle(10)
    c+=10
    assert(c.radius==20)

def test_aug_mul():
    c = Circle(10)
    c *= 10
    assert(c.radius == 60)
