#!/usr/bin/env python3


class keezer_display_stdout(keezer_display):
    """ Output class for keezer management project """


    def __init__(self):
        """ Register self with driver """
        super().__init__(self)
        self.data = []


    def ingest(self, datum):
        self.data.append(datum)


    def do_output(self):
        print(__name__ + ":")
        for datum in self.data:
            print(datum)

        return True


if __name__ == "__main__":
    outp = keezer_display()
    assert(outp.do_output())
