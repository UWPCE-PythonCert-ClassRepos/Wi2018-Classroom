#!/usr/bin/env python3


class KOutput:
    """ Output class for keezer management project """


    def __init__(self):
        """ Register self with driver """
        pass


    def ingest(self, datum):
        """ Take data from driver """
        pass


    def do_output(self):
        """ Show configured output """
        return True


if __name__ == "__main__":
    outp = KOutput()
    assert(outp.do_output())
