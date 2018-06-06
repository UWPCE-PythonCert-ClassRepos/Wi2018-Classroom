"""
Unit tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump import Pump
from sensor import Sensor

from .controller import Controller
from .decider import Decider


class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class
    """

    def test_decider1(self):
        """Does it return 1 to pump in when below margins? """
        pump = Pump('127.0.0.1', 8000)
        pump.set_state = MagicMock(return_value=True)
        self.decider = Decider(100, 10)
        self.actions = {
        'PUMP_IN': pump.PUMP_IN,
        'PUMP_OUT': pump.PUMP_OUT,
        'PUMP_OFF': pump.PUMP_OFF,
    }
        assert self.decider.decide(50, "PUMP_IN", self.actions) == 1


    def test_decider2(self):
        """ Does it return 0 to shut off when within margins?"""
        pump = Pump('127.0.0.1', 8000)
        pump.set_state = MagicMock(return_value=True)
        self.decider = Decider(100, 10)
        self.actions = {
        'PUMP_IN': pump.PUMP_IN,
        'PUMP_OUT': pump.PUMP_OUT,
        'PUMP_OFF': pump.PUMP_OFF,
    }
        assert self.decider.decide(101, "PUMP_IN", self.actions) == 0

    def test_decider3(self):
        """Does it return -1 to pump out when above margin?"""
        pump = Pump('127.0.0.1', 8000)
        pump.set_state = MagicMock(return_value=True)
        self.decider = Decider(100, 10)
        self.actions = {
        'PUMP_IN': pump.PUMP_IN,
        'PUMP_OUT': pump.PUMP_OUT,
        'PUMP_OFF': pump.PUMP_OFF,
    }
        assert self.decider.decide(250, "PUMP_IN", self.actions) == -1

class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    # TODO: write a test or tests for each of the behaviors defined for
    #       Controller.tick


    def test_controller_tick(self):
        self.pump = Pump('127.0.0.1', 8000)
        self.pump.set_state = MagicMock(return_value = True)
        self.pump.get_state = MagicMock(return_value = "PUMP_IN") # Or a number?
        self.sensor = Sensor('127.0.0.1', 8000)
        self.sensor.measure = MagicMock(return_value = 20)
        self.decider = Decider(100, 10)
        self.controller = Controller(self.sensor, self.pump, self.decider)
        """assert this returns false, because I'm not set up with a server? """
        """ This is definitely wrong"""
        assert not self.controller.tick() 
    
