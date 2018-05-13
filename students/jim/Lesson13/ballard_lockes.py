import pdb


class Locke:

    def __init__(self, capacity):
        """
        :param capacity: the number of boats this locke can accept
        Lockes will be initialized with doors closed and pumps running.
        """
        self.capacity = capacity
        self.doors_open = False
        self.pumps_running = True

    def __enter__(self):
        print("Called enter dunder.")
        self.toggle_pumps()
        self.toggle_doors()
        return self

    def __exit__(self, exc, exc_val, tb):
        print("Called exit dunder.")

    def move_boats_through(self, num_boats):

        try:
            assert self.capacity >= num_boats
            print("Moved {} boats through successfully.".format(num_boats))
            print("Returning locke to original state...")
            self.__exit__(None, 0, 0)
        except AssertionError:
            print("Error: insufficient capacity!")
            print("Returning locke to original state...")
            self.__exit__(AssertionError, 0, 0)

    def toggle_doors(self):

        if self.doors_open:
            self.doors_open = False
            print("Doors have been closed.")
        else:
            self.doors_open = True
            print("Doors have been opened.")

    def toggle_pumps(self):

        if self.pumps_running:
            self.pumps_running = False
            print("Pumps have been stopped.")
        else:
            self.pumps_running = True
            print("Pumps have been started.")


small_locke = Locke(5)
big_locke = Locke(10)
boats = 8

with small_locke as locke:
    locke.move_boats_through(boats)

with big_locke as locke:
    locke.move_boats_through(boats)
