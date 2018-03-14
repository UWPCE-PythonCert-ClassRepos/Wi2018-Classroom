'''
Circle exercise
Goal: create a class that represents a circle.



Print the circle and get something nice.
Be able to add two circles together.
Be able to compare two circles to see which is bigger.
Be able to compare to see if they are are equal.
(follows from above) be able to put them in a list and sort them.


You will use:

properties.
a bunch of “magic methods”.
a classmethod (after you’ve learned about them…).
General Instructions:
For each step, write a couple of unit tests that test the new features.
Run these tests (and they will fail the first time)
Add the code required for your t.ests to pass.
'''

import math

class circle():
    def _init_ (self, radius = 2):
        self.radius=float(radius)
    
    @property
    def area():  #A=πr2
        return (self.radius**2)* math.pi 




