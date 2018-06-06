class C:
    _x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


class D():
    def __init__(self, x=5):
        self._x = 5

    @property
    def getx(self):
        """I am read only"""
        return self._x

    def __str__(self):
        return "Foo: {}".format(self._x)

#Callable object
class Quadratic:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    # without this method, q(2) below will fail
    def __call__(self, x):
        return self.A * x**2 + self.B * x + self.C

q = Quadratic(3, 2, 4)
test = q(2)
print(test)
