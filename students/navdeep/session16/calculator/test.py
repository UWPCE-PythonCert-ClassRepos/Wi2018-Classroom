"""
Performs Unit tests on the calculator class and
the classes that relate to calculator, including
adder, subtracter, divider, multiplier.
"""
from unittest import TestCase
from unittest.mock import MagicMock
from exceptions import InsufficientOperands
from adder import Adder
from subtracter import Subtracter
from multiplier import Multiplier
from divider import Divider
from calculator import Calculator
"""
Creates class to test the adder
"""
class AdderTests(TestCase):
	"""
	Tests the adder class
	"""
	def test_adding(self):
		adder = Adder()
		for i in range(-10, 10):
			for j in range(-10, 10):
				self.assertEqual(i + j, adder.calc(i, j))
"""
Creates class to test the subtracter
"""
class SubtracterTests(TestCase):
	"""
	Tests the subtracter class
	"""
	def test_subtracting(self):
		subtracter = Subtracter()
		for i in range(-10, 10):
			for j in range(-10, 10):
				self.assertEqual(i - j, subtracter.calc(i, j))
"""
Tests the Multiplier class
"""
class MultiplierTests(TestCase):
	"""
	Tests the multiplier class
	"""
	def test_multiplier(self):
		multiplier = Multiplier()
		for i in range(-10, 10):
			for j in range(-10, 10):
				self.assertEqual(i * j, multiplier.calc(i, j))
"""
Tests the Divider Class
"""
class DividerTests(TestCase):
	"""
	Tests the divider class
	"""
	def test_divider(self):
		divider = Divider()
		for i in range(1, 10):
			for j in range(1, 10):
				self.assertEqual(i / j, divider.calc(i, j))
"""
Tests the Calculator class's methods. We are testing to ensure the methods are properly called in the calculator class
"""
class CalculatorTests(TestCase):
	"""
	Instantiate the the adder, subtracter, multiplier and divider classes
	"""
	def setUp(self):
		self.adder = Adder()
		self.subtracter = Subtracter()
		self.multiplier = Multiplier()
		self.divider = Divider()
		self.calculator = Calculator(self.adder, self.subtracter, self.multiplier, self.divider)
	"""
	Test the insufficient operands exception
	"""
	def test_insufficient_operands(self):
		self.calculator.enter_number(0)
		with self.assertRaises(InsufficientOperands):
			self.calculator.add()
	"""
	Test that the add method in the calculator class is properly called
	"""
	def test_adder_call(self):
		self.adder.calc = MagicMock(return_value = 0)
		self.calculator.enter_number(1)
		self.calculator.enter_number(2)
		self.calculator.add()
		self.adder.calc.assert_called_with(1,2)
	"""
	Test that the subtract method in the calculator class is properly
	called
	"""
	def test_subtracter_call(self):
		self.subtracter.calc = MagicMock(return_value = 0)
		self.calculator.enter_number(1)
		self.calculator.enter_number(2)
		self.calculator.subtract()
		self.subtracter.calc.assert_called_with(1,2)
	"""
	Test the divider method in the calculator class is properly
	called
	"""
	def test_divider_call(self):
		self.divider.calc = MagicMock(return_value = 0)
		self.calculator.enter_number(1)
		self.calculator.enter_number(2)
		self.calculator.divide()
		self.divider.calc.assert_called_with(1,2)
	"""
    Test the multiplier method in the calculator class is properly
    called
    """
	def test_multiplier_call(self):
		self.multiplier.calc = MagicMock(return_value = 0)
		self.calculator.enter_number(1)
		self.calculator.enter_number(2)
		self.calculator.multiply()
		self.multiplier.calc.assert_called_with(1,2)
