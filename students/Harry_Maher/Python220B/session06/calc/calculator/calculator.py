#!/usr/bin/env python3
"""a claculator classs"""

from .exceptions import InsufficientOperands


class Calculator:

    def __init__(self, adder, subtracter, multiplier, divider):
        """The calculator is instantiated with an
        adder, subtracter, multiplyer, and divider,
        and an empty stack
        """
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """Push new entered numbers to the end of the stack"""
        self.stack.append(number)  # This corrects the order

    def _do_calc(self, operator):
        """Perform calculation on entered numbers using specified operator"""
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """call the adder function specified when instantiated"""
        return self._do_calc(self.adder)

    def subtract(self):
        """call the subtracter function specified when instantiated"""
        return self._do_calc(self.subtracter)

    def multiply(self):
        """call the multiplier function specified when instantiated"""
        return self._do_calc(self.multiplier)

    def divide(self):
        """call the divider function specified when instantiated"""
        return self._do_calc(self.divider)
