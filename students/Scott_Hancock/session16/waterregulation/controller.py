"""
Encapsulates command and coordination for the water-regulation module
"""
from pump import Pump
from sensor import Sensor


class Controller(object):
    """
    Encapsulates command and coordination for the water-regulation module
    """

    def __init__(self, sensor, pump, decider):
        """
        Create a new controller

        :param sensor: Typically an instance of sensor.Sensor
        :param pump: Typically an instance of pump.Pump
        :param decider: Typically an instance of decider.Decider
        """

        self.actions = {
            'PUMP_IN': pump.PUMP_IN,
            'PUMP_OUT': pump.PUMP_OUT,
            'PUMP_OFF': pump.PUMP_OFF,
        }
        
        self.sensor = sensor.Sensor('127.0.0.1', 8000)
        self.pump = pump.Pump('127.0.0.1', 8001)
        self.decider = decider.Decider(10, self.actions['PUMP_IN'], self.actions)

    def tick(self):
        """
        On each call to tick, the controller shall:

          1. query the sensor for the current height of liquid in the tank
          2. query the pump for its current state (pumping in, pumping out, or at rest)
          3. query the decider for the next appropriate state of the pump, given the above
          4. set the pump to that new state

        :return: True if the pump has acknowledged its new state, else False
        """

        # TODO: Implement the above-defined behaviors

        return None
