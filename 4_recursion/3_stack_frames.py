class Stack(object):
	"""Represents a stack ADT using a list."""

	def __init__(self):
		"""Initializes an empty stack."""

		self.items = []

	def add(self, item):
		"""Adds an item to the top of the stack."""

		self.items.append(item)

	def remove(self):
		"""Removes the last item from the top of the stack."""

		return self.items.pop()

	def is_empty(self):
		"""Checks if the stack is empty."""

		return self.items == []

	def size(self):
		"""Returns the number of items in the stack."""

		return len(self.items)


# Doesn't really work w/ Python 2 - never gets to 0.
rem_stack = Stack()

def convert_base(num, to_base):
	"""Converts an integer to a string repr of a given base."""

	digits = '0123456789ABCDEF'

	while num > 0:
		if num < to_base:
			print num
			rem_stack.add(digits[num])
		else:
			rem_stack.add(digits[num % to_base])
			num = num / to_base

	converted_str = ''
	while not rem_stack.is_empty():
		converted_str += rem_stack.remove()
	return converted_str

# print convert_base(10, 2)

