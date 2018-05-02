#!/usr/bin/env python3

# Ballard Locks
# rriehle 2018

# Lots of possibilities for the locke scenario,
# closures, multiple dispatch, finite state systems.


class Locke(object):

    def __init__(self, capacity=1):
        self.boat_capacity = capacity

    def __enter__(self):
        print("In __enter__(): Stopping the pumps")
        print("In __enter__(): Opening the doors.")
        print("In __enter__(): Closing the doors.")
        print("In __enter__(): Starting the pumps")
        return self

    def __exit__(self, *args):
        print("In __exit__(): Stopping the pumps")
        print("In __exit__(): Opening the other doors.")
        print("In __exit__(): Closing the other doors.")
        print("In __exit__(): Starting the pumps")

    def move_boats_through(self, num_boats=0):
        if num_boats > self.boat_capacity:
            raise ResourceWarning("{} is too many boats for this locke!".format(num_boats))
        print("Moving {} boats through the locke.".format(
            num_boats)
        )


def main():

    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8

    # Too many boats through a small locke will raise an exception
    with small_locke as locke:
        locke.move_boats_through(boats)

    # A lock with sufficient capacity can move boats without incident.
    with large_locke as locke:
        locke.move_boats_through(boats)


if __name__ == '__main__':
    main()
