#!/usr/bin/env python3

"""
https://canvas.uw.edu/courses/1188584/assignments/4189638?module_item_id=8331806

Write a context manager class Locke to simulate the overall functioning of the
system. When the locke is entered it stops the pumps, opens the doors, closes
the doors, and restarts the pumps. Likewise when the locke is exited it runs
through the same steps: it stops the pumps, opens the doors, closes the doors,
and restarts the pumps. Don’t worry for now that in the real world there are
both upstream and downstream doors, and that they should never be opened at the
same time; perhaps you’ll get to that later. During initialization the context
manger class accepts the locke’s capacity in number of boats. If someone tries
to move too many boats through the locke, anything over its established
capacity, raise a suitable error. Since this is a simulation you need do nothing
more than print what is happening with the doors and pumps, like this:

"Stopping the pumps."
"Opening the doors."
"Closing the doors."
"Restarting the pumps."
"""

class Locke:


    def __init__(self, cap = 1):
        self.capacity = cap


    def __enter__(self):
        print("Entering:")
        print("\tStopping the pumps.")
        print("\tOpening the doors.")
        print("\tClosing the doors.")
        print("\tRestarting the pumps.")

        return self


    def __exit__(self, *unused):
        print("Exiting:")
        print("\tStopping the pumps.")
        print("\tOpening the doors.")
        print("\tClosing the doors.")
        print("\tRestarting the pumps.")


    def move_boats_through(self, boats):
        if boats > self.capacity:
            raise ValueError(f"Attempted to send {boats} boats through lock "
                             f"with capacity {self.capacity}")

        print(f"Moving {boats} boats through lock.")


if __name__ == "__main__":
    lockes = [Locke(10), Locke(5)]
    boats = 8

    # A lock with sufficient capacity can move boats without incident.
    for l in lockes:
        with l as locke:
            print(f"Trying to move {boats} through lock with capacity {locke.capacity}:")
            try:
                locke.move_boats_through(boats)
            except ValueError as e:
                print("Moving boats failed.  Caught exception: ", e)
