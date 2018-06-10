#!/usr/bin/env python3

import random
import time
from keezer_sensor import keezer_sensor

class keezer_sensor_random(keezer_sensor):
    """ Generate random data """


    def __init__(self, bounds=(0, 100)):
        """ Register self with driver """
        assert len(bounds) == 2
        super().__init__(self)

        random.seed(time.time())
        self.data_gen = make_data_gen(bounds)


    def poll_sensor(self):
        # pylint: disable=missing-docstring
        return self.data_gen()


def make_data_gen(bounds):
    # pylint: disable=missing-docstring
    def gen():
        return random.randint(*bounds)


if __name__ == "__main__":
    sns = keezer_sensor()
    datum = sns.poll_sensor()
    assert datum > 0 and datum < 100

    sns = keezer_sensor_random((-100, 0))
    datum = sns.poll_sensor()
    assert datum > -100 and datum < 0
