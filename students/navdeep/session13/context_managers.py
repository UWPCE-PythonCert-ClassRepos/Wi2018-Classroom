class Locke(object):
	def __init__(self,cap_boats):
		self.cap = cap_boats

	def allow_boats(self, num_boats):
		if self.cap <= num_boats:
			return True
		else:
			return False

	def move_boats_through(self, num_boats):
		try:
			if not self.allow_boats(num_boats):
				raise RuntimeError
		except RuntimeError as e:
			print("Too many boats attempting to enter through Locke")
		finally:
			print("Closing the doors")
			
	def __enter__(self):
		print("Stopping the pumps\nOpening the doors")
		return self

	def __exit__(self, *args):
		print("Restarting the pumps")


small_locke = Locke(5)
large_locke = Locke(10)
boats = 8

with large_locke as locke:
	locke.move_boats_through(boats)

print()
with small_locke as locke:
	locke.move_boats_through(boats)



