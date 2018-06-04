class Locke(object):

    def __init__(self, capacity=1):
        self.capacity = capacity

    def __enter__(self):
        print("__enter__()")
        print("...stopping the pumps")
        print("...opening inbound doors")
        print("...closing inbound doors")
        print("...starting the pumps")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ResourceWarning:
            print("Too many boats going through locke")
        print("__exit__()")
        print("...stopping the pumps")
        print("...opening outbound doors")
        print("...closing outbound doors")
        print("...starting the pumps")
        return True

    def move_boats_through(self, boats=0):
        if boats > self.capacity:
            raise ResourceWarning()
        print("Moving {} boats successfully through the locke".format(boats))

if __name__ == '__main__':
    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8

    # Too many boats through a small locke will raise an exception
    with small_locke as locke:
        locke.move_boats_through(boats)

    # A lock with sufficient capacity can move boats without incident.
    with large_locke as locke:
        locke.move_boats_through(boats)