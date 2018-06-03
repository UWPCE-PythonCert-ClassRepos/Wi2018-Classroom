#!/usr/bin/env python3


class KOStdout(KOutput):
    """ Output class for keezer management project """


    def __init__(self):
        """ Register self with driver """
        super.__init__(self)
        self.data = []


    def ingest(self, datum):
        self.data.append(datum)


    def do_output(self):
        print(__name__ + ":")
        for datum in self.data:
            print(datum)

        return True


if __name__ == "__main__":
    outp = KOutput()
    assert(outp.do_output())
