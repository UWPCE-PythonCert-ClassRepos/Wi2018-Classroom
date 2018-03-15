from circle import Circle

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
