#!/usr/bin/env python3
"""A set of unit test(s) for calcuator"""

from unittest import TestCase
from unittest.mock import MagicMock

from calculator.adder import Adder
from calculator.subtracter import Subtracter
from calculator.multiplier import Multiplier
from calculator.divider import Divider
from calculator.calculator import Calculator
from calculator.exceptions import InsufficientOperands


class AdderTests(TestCase):
    """various adder test"""
    def test_adding(self):
        """Does the adder add? """
        adder = Adder()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i + j, adder.calc(i, j))


class SubtracterTests(TestCase):
    """various adder test"""
    def test_subtracting(self):
        """Does the ** do **? """
        subtracter = Subtracter()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i - j, subtracter.calc(i, j))


class MultiplierTests(TestCase):
    """various test"""
    def test_multiplying(self):
        """Does the ** do **? """
        multiplier = Multiplier()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i * j, multiplier.calc(i, j))


class DivisionTests(TestCase):
    """various  test"""
    def test_dividing(self):
        """Does the ** do **? """
        divider = Divider()

        for i in range(-10, 10, 3):
            for j in range(-10, 10, 3):
                self.assertEqual(i / j, divider.calc(i, j))


class CalculatorTests(TestCase):
    """various test"""
    def setUp(self):
        """Set up for calc tests so don't have to rewrite"""
        self.adder = Adder()
        self.subtracter = Subtracter()
        self.multiplier = Multiplier()
        self.divider = Divider()
        # Line is too long, but whatever.
        self.calculator = Calculator(self.adder, self.subtracter, self.multiplier, self.divider)

    def test_insufficient_operands(self):
        """Will it  raise an error when there aren't enough operands?"""
        self.calculator.enter_number(0)

        with self.assertRaises(InsufficientOperands):
            self.calculator.add()

    def test_adder_call(self):
        """Does adder call adder in the right order?"""
        self.adder.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.add()

        self.adder.calc.assert_called_with(1, 2)

    def test_subtracter_call(self):
        """Does subtractor call subtractor in the right order?"""
        self.subtracter.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.subtract()
        self.subtracter.calc.assert_called_with(1, 2)
