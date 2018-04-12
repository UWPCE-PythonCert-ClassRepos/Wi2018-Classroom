import circle

def test_area():
    my_circle = Circle(3)
    assert my_circle.area == math.pi * 3**2

def test_repr():
    my_circle = Circle(4)
    assert eval(repr(my_circle)) == Circle(4)