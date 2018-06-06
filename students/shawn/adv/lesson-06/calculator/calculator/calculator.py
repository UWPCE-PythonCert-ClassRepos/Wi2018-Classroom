"""Calculator"""


from .exceptions import InsufficientOperands


class Calculator(object):
    """Calculator"""

    def __init__(self, adder, subtracter, multiplier, divider):
        """
        Initialization
        :param adder:
        :param subtracter:
        :param multiplier:
        :param divider:
        """

        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """
        Add number to stack
        :param number:
        :return: list
        """

        self.stack.append(number)

    def _do_calc(self, operator):
        """
        Return results of operation on last two numbers in stack
        :param operator:
        :return: number
        """

        try:
            result = operator.calc(self.stack[-2], self.stack[-1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """
        Add
        :return: sum
        """

        return self._do_calc(self.adder)

    def subtract(self):
        """
        Subtract
        :return: difference
        """

        return self._do_calc(self.subtracter)

    def multiply(self):
        """
        Multiply
        :return: factor
        """

        return self._do_calc(self.multiplier)

    def divide(self):
        """
        divide
        :return: quotient
        """

        return self._do_calc(self.divider)
