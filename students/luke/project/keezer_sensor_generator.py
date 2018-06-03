#!/usr/bin/env python3

import keezer_sensor
import random
import time

class KSGen(KSensor):
    """ Use a generator to produce datapoints """


    def __init__(self, bounds = (0, 100)):
        assert(len(bounds) == 2)
        """ Register self with driver """
        super.__init__(self)

        random.seed(time.time())
        self.data_gen = make_data_gen(bounds)


    def poll_sensor(self):
        return data_gen()


    def make_data_gen(bounds):
        def gen(bounds):
            while True:
                yield random.randint(*bounds)
        return gen



if __name__ == "__main__":
    sns = KSGen()
    datum = sns.poll_sensor()
    assert(datum > 0 && datum < 100)

    sns = KSGen((-100, 0)
    datum = sns.poll_sensor()
    assert(datum > -100 && datum < 0)
