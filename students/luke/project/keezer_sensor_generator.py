#!/usr/bin/env python3
""" Use a generator to produce datapoints """

import random
import time
from keezer_sensor import KSensor

class KSGenerator(KSensor):
    """ Use a generator to produce datapoints """


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
        while True:
            yield random.randint(*bounds)
    return gen


if __name__ == "__main__":
    sns = KSGenerator()
    datum = sns.poll_sensor()
    assert datum > 0 and datum < 100

    sns = KSGenerator((-100, 0))
    datum = sns.poll_sensor()
    assert datum > -100 and datum < 0
