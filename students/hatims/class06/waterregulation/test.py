"""
Unit tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

import controller
#from controller import Controller
from decider import Decider

ACTIONS = {
    'PUMP_IN': 1,
    'PUMP_OUT': -1,
    'PUMP_OFF': 0,
}

class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class
    """

    def test_decide(self):
        decider = Decider(100, 0.05)
        self.assertEqual(ACTIONS['PUMP_IN'], decider.decide(90, ACTIONS['PUMP_OFF'], ACTIONS))
        self.assertEqual(ACTIONS['PUMP_OUT'], decider.decide(110, ACTIONS['PUMP_OFF'], ACTIONS))
        self.assertEqual(ACTIONS['PUMP_OFF'], decider.decide(95, ACTIONS['PUMP_OFF'], ACTIONS))
        self.assertEqual(ACTIONS['PUMP_OFF'], decider.decide(105, ACTIONS['PUMP_OFF'], ACTIONS))

        self.assertEqual(ACTIONS['PUMP_OFF'], decider.decide(110, ACTIONS['PUMP_IN'], ACTIONS))
        self.assertEqual(ACTIONS['PUMP_IN'], decider.decide(90, ACTIONS['PUMP_IN'], ACTIONS))

        self.assertEqual(ACTIONS['PUMP_OFF'], decider.decide(90, ACTIONS['PUMP_OUT'], ACTIONS))
        self.assertEqual(ACTIONS['PUMP_OUT'], decider.decide(110, ACTIONS['PUMP_OUT'], ACTIONS))

class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    def test_tick(self):
        self.sensor = Sensor('127.0.0.1', '8000')
        self.pump = Pump('127.0.0.1', '8000')
        self.decider = Decider(100, 0.05)
        self._controller = controller.Controller(self.sensor, self.pump, self.decider)
        self.pump.set_state = MagicMock(return_value=True)
        self.pump.get_state = MagicMock(return_value=True)
        self.sensor.measure = MagicMock(return_value=True)
        self.decider.decide = MagicMock(return_value=True)
        self._controller.tick()

        self.pump.set_state.assert_called_with(True)
        self.pump.get_state.assert_called_with()
        self.sensor.measure.assert_called_with()
        self.decider.decide.assert_called_with(True, True, ACTIONS)
