"""
Module tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from .controller import Controller
from .decider import Decider


class ModuleTests(unittest.TestCase):
    """
    Module tests for the water-regulation module
    """

    # TODO: write an integration test that combines controller and decider,
    #       using a MOCKED sensor and pump.

    def test_integration(self):
        """ An integration test"""
        self.pump = Pump('127.0.0.1', 8000)
        self.pump.set_state = MagicMock(return_value = True)
        self.pump.get_state = MagicMock(return_value = "PUMP_IN") # Or a number?
        self.sensor = Sensor('127.0.0.1', 8000)
        self.sensor.measure = MagicMock(return_value = 20)
        self.decider = Decider(100, 10)
        self.controller = Controller(self.sensor, self.pump, self.decider)

        self.controller.tick()

