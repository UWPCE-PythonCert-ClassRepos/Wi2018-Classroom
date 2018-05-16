#!/usr/bin/env python3
#Ballard Locke exercise

class Locke:

    def __init__(self, cap=1, num_boats=1):
        self.capacity = cap
        self.boats = num_boats

    def __enter__(self):
        print('Entering: Stopping the pumps')
        print('Entering: Opening the doors')
        print('Entering: Closing the doors')
        print('Entering: Restarting the pumps')
        return self

    def __exit__(self, *args):
        print('Exiting: Stopping the pumps')
        print('Exiting: Opening the doors')
        print('Exiting: Closing the doors')
        print('Exiting: Restarting the pumps')

    def move_boats_through(self,num_boats=0):
        if num_boats > self.capacity:
            raise ValueError (f'{num_boats} boats exceed the locke capacity of {self.capacity}!')
        print (f'Moving {num_boats} boats through the locke...')

def main():

    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8

    # Too many boats through a small locke will raise an exception
    with small_locke as locke:
        try:
            locke.move_boats_through(boats)
        except ValueError as e:
            print (f'Exception: {e}')


    # A lock with sufficient capacity can move boats without incident.
    with large_locke as locke2:
        try:
            locke2.move_boats_through(boats)
        except ValueError as e:
            print(f'Exception: {e}')


if __name__ == '__main__':
    main()
