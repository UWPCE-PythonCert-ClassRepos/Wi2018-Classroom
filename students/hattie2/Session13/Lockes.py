
class Locke(object):
    def __init__(self, size):
        print('Locke, size ' + str(size)+ ' Created')
        self.size = size

    def __enter__(self):
        print("Opening Lock")
        print("Stopping pump\n Opening doors \n Wait")
        input("Are boats loaded? Conditions safe? Hit Enter")
        print("Closing doors\n restarting pumps")
        return print("Boats loaded.")

    def __exit__(self, type, value, tb):
        return ("Boats done\n\n")

    def move_boats_through(self, ships):
        try:
            if ships > self.size:
                raise ValueError('Exception: Oops, too many boats')
        except ValueError as err:
            print(err.args)


if __name__ == "__main__":

    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8

    print("\n\n\nMoving 8 boats into small locke.")
    with small_locke as locke:
        small_locke.move_boats_through(boats)

    print("\n\n\nMoving 8 boats into large locke.")
    with large_locke as locke:
        large_locke.move_boats_through(boats)
