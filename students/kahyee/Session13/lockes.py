

class Locke():
    """
    context manager class for lock system
    """
    def __init__(self, capacity):
        self.capacity = capacity
    
    def __enter__(self):
        print("Stopping the pumps./nOpening the doors./nClosing the doors./nRestarting the pumps.")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        


if __name__ == ""__main__"":
    
    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8

    # Too many boats through a small locke will raise an exception
    with small_locke as locke:
        locke.move_boats_through(boats)

    # A lock with sufficient capacity can move boats without incident.
    with large_locke as locke:
        locke.move_boats_through(boats)

    