# Tower of Hanoi - specs
# Three poles
# Need to move tower of ascending-size disks from one pole to another
# Can only put smaller disks on top of larger disks
# Probably makes sense to use three stacks to represent this
# Recursively solve this - base case is you have one disk
# Case to decrease problem size - move tower of size - 1

class Stack(object):
	"""Represents a stack ADT."""

	def __init__(self):
		"""Initializes the empty stack."""

		self.items = []

	def add(self, item):
		"""Adds an item to the top of the stack."""

		self.items.append(item)

	def remove(self):
		"""Removes and returns the top item in the stack."""

		if self.is_empty():
			return None
		else:
			return self.items.pop()

	def is_empty(self):
		"""Checks if the stack is empty."""

		return self.items == []

	def size(self):
		"""Returns number of items in the stack."""

		return len(self.items)

def move_tower(height, from_pole, to_pole, with_pole):
	"""Moves a tower of given height."""

	if height >= 1:
		move_tower(height - 1, from_pole, with_pole, to_pole)
		move_disk(from_pole, to_pole)
		move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(from_pole, to_pole):
	"""Moves a disk from and to given poles."""

	print 'Moving disk from %s to %s.' % (from_pole, to_pole)

# move_tower(3, 'Start', 'End', 'Mid')

def move_tower(height, from_pole, to_pole, with_pole):
	"""Moves a tower of a given height."""

	if height >= 1:
		move_tower(height - 1, from_pole, with_pole, to_pole)
		move_disk(from_pole, to_pole)
		move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(from_pole, to_pole):
	print 'Moving disk from %s to %s.' % (from_pole, to_pole)

move_tower(3, 'Start', 'End', 'Mid')