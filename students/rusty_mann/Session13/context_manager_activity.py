
class Locke(object):
    """
    """
    def __init__(self, capacity):
        self.capacity = capacity
        #self.handle_error = handle_error
        
    def move_boats_through(self, quantity):
        self.quantity = quantity
        if quantity > self.capacity:
            print("Too many boats")
            raise ValueError("Do not proceed")
        else:
            print("Proceed")
    
    def __enter__(self):
        print("Stopping the pumps.Opening the doors.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (exc_type, exc_val, exc_tb) == (None, None, None):
            pass
        else:
            print('{}, {}, {}'.format(exc_type, exc_val, exc_tb))
        print(".Closing the doors.Restarting the pumps.")
        return True

small_locke = Locke(5)
large_locke = Locke(10)
boats = 8

with small_locke as locke:
    locke.move_boats_through(boats)

with large_locke as locke:
    locke.move_boats_through(boats)

