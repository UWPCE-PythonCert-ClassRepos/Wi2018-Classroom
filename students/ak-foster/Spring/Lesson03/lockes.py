#!/usr/bin/env python3

class Locke():
    def __init__(self, limit, boats):
        self.limit = limit
        self.boats = boats
        self.actions = ["Stopping the pumps.", "Opening the doors.", "Closing the doors.", "Restarting the pumps."]

    def __enter__(self):
        [print(step) for step in self.actions]
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        [print(step) for step in self.actions]
        if exc_type:
            print(exc_type)

    def move_boats(self):
        if self.boats > self.limit:
            raise  Exception("Too many boats!").with_traceback(None)
        else:
            print(f"Moving {self.boats} boat(s) through the locks.")

s_locke = Locke(5, 8)
l_locke = Locke(10, 8)

# s_locke.move_boats()
# l_locke.move_boats()
