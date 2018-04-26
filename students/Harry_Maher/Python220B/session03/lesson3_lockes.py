#!/usr/bin/env python3
"""
Context managers!

"""
from time import sleep

class Locke: 

    steps = ["Stopping the pumps.", "Opening the doors.", "Closing the doors.", "Restarting the pumps."]

    def __init__(self, boats):
        self.max_boats = boats


    def __enter__(self):
        for step in self.steps:
            print(step)
            sleep(.5) # the lock is fast
        return self

    def move_boats_through(self, boats):
        if boats > self.max_boats:
            raise OverflowError("Boat overflow!") # is this where this goes?

    def __exit__(self, exc_type, exc_val, exc_tb):
        for step in self.steps:
            print(step)
            sleep(.5)



small_locke = Locke(5)
large_locke = Locke(10)
boats = 8


# # Too many boats through a small locke will raise an OverfloatError exception
# with small_locke as locke:
#     locke.move_boats_through(boats)

# # A lock with sufficient capacity can move boats without incident.
with large_locke as locke:
    locke.move_boats_through(boats)

# """
# with a contextmanager decorator
# """

# from contextlib import contextmanager

# @contextmanager
# class Locke2:
#     print("")