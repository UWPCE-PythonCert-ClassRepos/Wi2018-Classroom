from exceptions import InsufficientOperands
"""
This class will perform the calculator functions.
The calculations performed are addition, subtraction,
division, multiplication.
"""


class Calculator(object):

    def __init__(self, adder, subtracter, multiplier, divider):
        """
        Initializes the calculator class.  Initializes 
        the operations
        adder: the adder() class
        subtracter: the subtracter() class
        multiplier: the multiplier() class
        divider: the divider() class
        a list holding the integers is also initialized here
        """
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider
        self.stack = []

    def enter_number(self, number):
        """
        Appends a new number to the stack
        number: the number to be appended 
        to the stack
        """
        self.stack.append(number)

    def _do_calc(self, operator):
        """
        Performs a calculation on the two numbers stored 
        in the stack
        operator: the mathematical operation we are 
        performing on the numbers
        stored in the stack. The operator will be 
        either the adder, subtracter,
        divider or multiplier class.
        return: returns the result of the 
        mathematical operation
        """
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands
        else:
            self.stack = [result]
            return result

    def add(self):
        """
        Calls the adder class
        return: returns the adder class as the
        operation we are going to perform
        in the _do_calc method.
        """
        return self._do_calc(self.adder)

    def subtract(self):
        """
        Calls the subtracter class
        return: returns the subtracter class as
        the operation we are going to
        perform in the _do_calc method.
        """
        return self._do_calc(self.subtracter)

    def multiply(self):
        """
        Calls the multiplier class
        return: returns the multiplier class
        as the operation we are going to
        perform in the _do_calc method.
        """
        return self._do_calc(self.multiplier)

    def divide(self):
        """
        Calls the divider class
        return: returns the divider class as
        the operation we are going to
        perform in the _do_calc method.
        """
        return self._do_calc(self.divider)
