"""
Unit tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from waterregulation import controller as Controller
from waterregulation import decider as Decider


class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Decider.decide

    def test_setup(self):
        """
        Set values for tests that follow
        """
        self.sensor = Sensor('127.0.0.1', 8000)
        self.pump = Pump('127.0.0.1', 8000)
        self.decider = Decider(100, .05)
        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_decider_below(self):
        """Test that pump will pump in when below threshold """
        below = self.decider.decide(50, "PUMP_IN", self.actions) == 1
        assert below == 1

    def test_decider_ok(self):
        """Tests that pump shuts off when within parameters"""
        ok = self.decider.decide(400, self.controller.actions['PUMP_IN'], self.controller.actions)
        assert ok == 0

    def test_decider_above(self):
        """Tests that pumps will pump out when above threshold"""
        above = self.decider.decide(200, self.controller.actions['PUMP_IN'], self.controller.actions)
        assert above == -1

class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Controller.tick

    def test_setup(self):
        """
        Set values for tests that follow
        """
        self.sensor = Sensor('127.0.0.1', 8000)
        self.pump = Pump('127.0.0.1', 8000)
        self.decider = Decider(100, .05)
        self.controller = Controller(self.sensor, self.pump, self.decider)

    def test_pump(self):
        """
        Test functionality of the controller .
        """
        self.pump.set_state = MagicMock(return_value = True)
        self.pump.get_state = MagicMock(return_value = True)
        self.sensor.measure = MagicMock(return_value = True)
        self.decider.decide = MagicMock(return_value = True)
        self.controller.tick()
        assert self.pump.set_state == True
        assert self.pump.get_state == True
        assert self.sensor.measure == True
        assert self.decider.decide == True