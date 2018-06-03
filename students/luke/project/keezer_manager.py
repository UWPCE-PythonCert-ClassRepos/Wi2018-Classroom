#!/usr/bin/env python3

"""
Keezer management project.  See README.md
"""

import keezer_sensor as sns
import keezer_output as outp

class KeezerManager:
    """
    Driver class for keezer manager.  Sensors register with driver, which
    polls them periodically.  Output devices register with driver, which
    passes sensor polling data to them.
    """

    def __init__(self):
        self.sensors = []
        self.outputs = []


    def register_sensor(self, sns):
        self.sensors.append(sns)


    def register_output(self, outp):
        self.outputs.append(outp)


if __name__ == "__main__":
    kman = KeezerManager
    sns = sns.KSensor
    outp = outp.KOutput

    # Assert that sensor and output have registered with keezer manager
    assert(len(kman.sensors) == 1)
    assert(len(kman.outputs) == 1)
