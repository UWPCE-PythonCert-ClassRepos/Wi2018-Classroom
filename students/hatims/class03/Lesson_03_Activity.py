#!/usr/bin/env python

#from contextlib import contextmanager


class Locke(object):
        """
        Context manager class to handle Balard Locke overall functioning
        """

        def __init__(self, boatCapacity):
            self.boatCapacity = boatCapacity

        def __enter__(self):
            print("ENTERING\n")
            print("Stopping the pumps.")
            print("Opening the doors.")
            print("Closing the doors.")
            print("Restarting the pumps.\n") 
            return self

        def __exit__(self, *args):
            print("EXISTING\n")
            print("Stopping the pumps.")
            print("Opening the doors.")
            print("Closing the doors.")
            print("Restarting the pumps.") 
            

        def move_boats_through(self, boats):
            if boats > self.boatCapacity:
                raise Exception("Locke exceeded capacity, expected {}, but {} were given.".format(self.boatCapacity, boats)) 
            else:
                print("All boats have been moved through the locke")
            

if __name__ == "__main__":
    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8

with large_locke as locke:
    locke.move_boats_through(boats)

with small_locke as locke:
    locke.move_boats_through(boats)

