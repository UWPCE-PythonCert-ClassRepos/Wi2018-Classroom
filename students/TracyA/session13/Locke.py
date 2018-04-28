#!/usr/bin/env python

from contextlib import contextmanager

# Programming in Python B Spring 2018
# April 25, 2018
# Lession 03 - saved in Session13 -
# Ballard Locks
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom
# Create a class Locke that has:
#      __init__: takes the capacity of boats per locke
#      __enter__: prints "Stopping the pump."
#                                   "Opening the doors."
#                                   "Closing the doors."
#                                   "Restarting the pumps."
#  move_boats_through(boats) method: if locke capacity < boats raise an error
#  __exit__: prints same as enter


@contextmanager
def Locke(capacity):
    try:
        print("Stopping the pump.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")
        yield WithinContext(capacity)
    except ValueError:
        print("Bound Exception Found: Too many boats through a small locke.")
    finally:
        print("Stopping the pump.")
        print("Opening the doors.")
        print("Closing the doors.")
        print("Restarting the pumps.")


class WithinContext(object):
    def __init__(self, capacity):
        self.capacity = capacity

    def move_boats_through(self, boats):
        """
        Method to check if Locke is large enough
        boats and boats passing through locke
        returns None or Value error
        """
        if boats > self.capacity:
            raise ValueError
        else:
            print("Locke has sufficient capacity for the boats.")


small_locke = Locke(5)
large_locke = Locke(10)
boats = 8

# Too many boats through a small locke will raise an exception
with small_locke as locke:
    locke.move_boats_through(boats)

# A lock with sufficient capacity can move boats without incident.
with large_locke as locke:
    locke.move_boats_through(boats)
