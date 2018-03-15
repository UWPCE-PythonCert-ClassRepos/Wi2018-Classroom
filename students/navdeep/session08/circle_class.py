import math

class Circle():
	def __init__(self, radius = 4):
		self.radius = float(radius)

	@property
	def area(self):
		return math.pi * self.radius**2

	@classmethod
	def from_diameter(cls, diameter):
		return cls(diameter / 2)

	@property
	def diameter(self):
		return 2 * self.radius

	@diameter.setter
	def diameter(self, diameter):
		self.radius = diameter / 2


	def __str__(self):
		return "Circle with radius: {:.6f}".format(self.radius)

	def __repr__(self):
		return "Circle({})".format(int(self.radius))

	def __add__(self,other):
		if type(other) == int or type(other) == float:
			return Circle(self.radius + other)
		else:
			return Circle(self.radius + other.radius)


	def __iadd__(self,other):
		if type(other) == int or type(other) == float:
			new_radius = self.radius + other
		else:
			new_radius = self.radius + other.radius
		self.radius = new_radius
		return self #why return self instead of self.radius?

	def __isub__(self,other):
		if type(other) == int or type(other) == float:
			new_radius = self.radius - other
		else:
			new_radius = self.radius - other.radius
		self.radius = new_radius
		return self

	def __imul__(self,other):
		if type(other) == int or type(other) == float:
			new_radius = self.radius * other
		else:
			new_radius = self.radius * other.radius
		self.radius = new_radius
		return self

	def __mul__(self, val):
		return Circle(self.radius * val)

	def __lt__(self,other):
		return ((self.radius) < (other.radius))

	def __gt__(self,other):
		return (self.radius) > (other.radius)

	def __eq__(self,other):
		return self.radius == other.radius

	def __radd__(self,other):
		return Circle.__add__(self,other)

	def __rmul__(self, other):
		return Circle.__mul__(self,other)

	@staticmethod
	def sort_key(self):
		return self.radius


class Sphere(Circle):
	
	def __init__(self,radius = 4):
		super().__init__(radius)

	def __str__(self):
		return "Sphere with radius: {:.6f}".format(self.radius)

	def __repr__(self):
		return "Sphere({})".format(int(self.radius))

	@property
	def volume(self):
		return (4.0/3.0) * math.pi * self.radius ** 3

	@property
	def area(self):
		return 4*math.pi*self.radius**2





