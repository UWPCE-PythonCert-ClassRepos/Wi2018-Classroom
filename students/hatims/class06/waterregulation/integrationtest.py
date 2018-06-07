"""
Module tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from controller import Controller
from decider import Decider


class ModuleTests(unittest.TestCase):
    """
    Module tests for the water-regulation module
    """

    def test_waterregulation_system(self):
        self.sensor = Sensor('127.0.0.1', '8000')
        self.pump = Pump('127.0.0.1', '8000')
        self.decider = Decider(100, 0.05)
        self.controller = Controller(self.sensor, self.pump, self.decider)

        self.pump.set_state = MagicMock(return_value=True)
        self.pump.get_state = MagicMock(return_value=True)
        self.sensor.measure = MagicMock(return_value=True)
        self.decider.decide = MagicMock(return_value=True)
        self.controller.tick()
        self.pump.set_state.assert_called_with(True)
        self.pump.get_state.assert_called_with()
        self.sensor.measure.assert_called_with()
        self.decider.decide.assert_called_with(True, True, self.controller.actions)
