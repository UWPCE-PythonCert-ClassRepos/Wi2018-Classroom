"""
Unit tests for the water-regulation module
"""
import unittest
from unittest.mock import MagicMock
from waterregulation.pump import Pump
from waterregulation.sensor import Sensor
from waterregulation.controller import Controller
from waterregulation.decider import Decider
class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class
    """
    # TODO: write a test or tests for each of the behaviors defined for
    #       Decider.decide
    def setUp(self):
    	"""
    	Instantiates the pump, decider, sensor, and controller classes
    	"""
        self.pump = Pump('127.0.0.1', 514)
        self.decider = Decider(100, .01)
        self.sensor = Sensor('127.0.0.1', 514)
        self.controller = Controller(self.sensor, self.pump, self.decider)
    def test_decider(self):
    	"""
    	Tests the functionality of the decider class and the decide method
    	"""
        return_value_off = self.decider.decide(200, self.controller.actions['PUMP_IN'], self.controller.actions)
        return_value_in = self.decider.decide(50, self.controller.actions['PUMP_OFF'], self.controller.actions)
        return_value_out = self.decider.decide(200, self.controller.actions['PUMP_OUT'], self.controller.actions)
        self.assertEqual(0, return_value_off)
        self.assertEqual(1, return_value_in)
        self.assertEqual(-1, return_value_out)

class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    #TODO: write a test or tests for each of the behaviors defined for
    #Controller.tick
    def setUp(self):
        """
        Instantiates the pump, decider, sensor and controller classes
        """
        self.pump = Pump('127.0.0.1', 514)
        self.sensor = Sensor('127.0.0.1', 514)
        self.decider = Decider(100, .01)
        self.controller = Controller(self.sensor, self.pump, self.decider)
    def test_pump_call(self):
        """
        Tests the functionality of the controller class and the tick method
        """
        self.pump.set_state = MagicMock(return_value = True)
        self.pump.get_state = MagicMock(return_value = True)
        self.sensor.measure = MagicMock(return_value = True)
        self.decider.decide = MagicMock(return_value = True)
        self.controller.tick()
        self.pump.set_state.assert_called_with(True)
        self.pump.get_state.assert_called_with()
        self.sensor.measure.assert_called_with()
        self.decider.decide.assert_called_with(True, True, self.controller.actions)
