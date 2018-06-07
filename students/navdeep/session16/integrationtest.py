"""
Module tests for the water-regulation module
"""
import unittest
from unittest.mock import MagicMock
from waterregulation.pump import Pump
from waterregulation.sensor import Sensor
from waterregulation.controller import Controller
from waterregulation.decider import Decider
class ModuleTests(unittest.TestCase):
    """
    Module tests for the water-regulation module
    """
    #TODO: write an integration test that combines controller and decider,
    #using a MOCKED sensor and pump.
    def test_module(self):
        """
        Tests the functionality of the water regulation classes and methods
        within those classes
        """
        self.pump = Pump('0.0.0.0', 514)
        self.sensor = Sensor('0.0.0.0', 514)
        self.decider = Decider(100,.01)
        self.control = Controller(self.sensor, self.pump, self.decider)
        self.pump.get_state = MagicMock(return_value = 0)
        current_state = self.pump.get_state()
        self.sensor.measure = MagicMock(return_value = 50)
        current_height = self.sensor.measure()
        new_state = self.decider.decide(current_height, current_state, self.control.actions)
        self.assertEqual(1, new_state)
