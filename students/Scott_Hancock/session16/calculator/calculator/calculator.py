""" Calculator built using dependency injection """

from .exceptions import InsufficientOperands

class Calculator(object):
    """ Calculator built using dependency injection """

    def __init__(self, adder, subtracter, multiplier, divider):
        """ Initialize calculator with adder, subtractor,
        multiplier, divider components """
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """ Place a number on the stack """
        self.stack.append(number)

    def _do_calc(self, operator):
        """ Add result to stack and return result """
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """ Add using adder module """
        return self._do_calc(self.adder)

    def subtract(self):
        """ Substract using subtracter module """
        return self._do_calc(self.subtracter)

    def multiply(self):
        """ Multiply using multiplier module """
        return self._do_calc(self.multiplier)

    def divide(self):
        """ Divide using divider module """
        return self._do_calc(self.divider)
