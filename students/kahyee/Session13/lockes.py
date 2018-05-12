

class Locke():
    """
    context manager class for lock system
    """
    def __init__(self, capacity):
        self.capacity = capacity
    
    def __enter__(self):
        print("Stopping the pumps.\nOpening the doors.")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ValueError:
            print("Too many boats for locke capacity, max number is {}".format(self.capacity))
        print("Closing the doors.\nRestarting the pumps.\n")
        return True
        
    def move_boats_through(self, num_boats):
        if self.capacity < num_boats:
            raise ValueError
        print("Successfully moving {} boats through locke".format(num_boats))

if __name__ == "__main__":
    
    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8

    # Too many boats through a small locke will raise an exception
    with small_locke as locke:
        locke.move_boats_through(boats)

    # A lock with sufficient capacity can move boats without incident.
    with large_locke as locke:
        locke.move_boats_through(boats)

    