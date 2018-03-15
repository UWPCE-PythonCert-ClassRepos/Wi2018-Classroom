from circle_class import Circle, Sphere
import math
import pytest

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
	assert my_circle.area == math.pi * my_circle.radius ** 2

def test_set_no_area():
	my_circle = Circle(3)
	with pytest.raises(AttributeError):
		my_circle.area = 20

def test_str():
	my_circle = Circle(4)
	assert str(my_circle) == "Circle with radius: 4.000000"

def test_repr():
	my_circle = Circle(4)
	assert repr(my_circle) == "Circle(4)"

def test_add():
	my_circle_1 = Circle(2)
	my_circle_2 = Circle(4)
	my_circle_3 = my_circle_1 + my_circle_2
	assert str(my_circle_3) == "Circle with radius: 6.000000"
	assert repr(my_circle_3) == "Circle(6)"

def test_multiply():
	my_circle = Circle(4)
	my_circle_2 = my_circle * 3
	assert str(my_circle_2) == "Circle with radius: 12.000000"
	assert repr(my_circle_2) == "Circle(12)"

def test_less_than():
	my_circle_1 = Circle(2)
	my_circle_2 = Circle(4)
	assert (my_circle_1 < my_circle_2) == True

def test_greater_than():
	my_circle_1 = Circle(2)
	my_circle_2 = Circle(4)
	assert (my_circle_1 > my_circle_2) == False

def test_equal_to():
	my_circle_1 = Circle(2)
	my_circle_2 = Circle(4)
	assert (my_circle_1 == my_circle_2) == False

def test_plus_equals():
	my_circle_1 = Circle(2)
	increase_radius = 10
	my_circle_1 += increase_radius
	assert str(my_circle_1) == "Circle with radius: 12.000000"

def test_plus_equals_object():
	my_circle_1 = Circle(2)
	my_circle_2 = Circle(4)
	my_circle_1 += my_circle_2
	assert str(my_circle_1) == "Circle with radius: 6.000000"

def test_reflect_mult():
	my_circle_1 = Circle(4)
	my_circle_2 = 3 * my_circle_1
	assert str(my_circle_2) == "Circle with radius: 12.000000"

def test_reflect_add():
	my_circle_1 = Circle(4)
	my_circle_2 = 4 + my_circle_1
	assert str(my_circle_2) == "Circle with radius: 8.000000"
	my_circle_3 = my_circle_1 + 10
	assert str(my_circle_3) == "Circle with radius: 14.000000"

def test_augment_add():
	my_circle_1 = Circle(4)
	my_circle_1 += 2
	assert my_circle_1.radius == 6.0
	my_circle_2 = Circle(2)
	my_circle_3 = Circle(3)
	my_circle_2 += my_circle_3
	assert my_circle_2.radius == 5.0

def test_augment_subtract():
	my_circle_1 = Circle(4)
	my_circle_1 -= 2
	assert my_circle_1.radius == 2.0
	my_circle_2 = Circle(3)
	my_circle_3 = Circle(2)
	my_circle_2 -= my_circle_3
	assert my_circle_2.radius == 1.0

def test_augment_multiply():
	my_circle_1 = Circle(4)
	my_circle_1 *= 2
	assert my_circle_1.radius == 8.0
	my_circle_2 = Circle(2)
	my_circle_3 = Circle(3)
	my_circle_2 *= my_circle_3
	assert my_circle_2.radius == 6.0

def test_from_diameter():
	diam = Circle.from_diameter(10)
	assert diam.radius == 5.0

def test_sort():
	circles = [Circle(6), Circle(7), Circle(2)]
	circles = sorted(circles, key = Circle.sort_key)
	assert circles == [Circle(2), Circle(6), Circle(7)]

def test_sphere_str():
	my_sphere = Sphere(4)
	assert str(my_sphere) == "Sphere with radius: 4.000000"

def test_repr():
	my_sphere = Sphere(4)
	assert repr(my_sphere) == "Sphere(4)"

def test_sphere_volume():
	my_sphere = Sphere(4)
	assert my_sphere.volume == (4.0/3.0) * math.pi * 4 ** 3

def test_sphere_surface_area():
	my_sphere = Sphere(4)
	assert my_sphere.area == 4*math.pi*4**2





