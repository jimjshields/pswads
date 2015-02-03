# Implementing a Deque in Python

class Deque(object):
	"""Represents a deque ADT."""

	def __init__(self):
		"""Initializes an empty deque."""

		self.items = []

	def add_front(self, item):
		"""Adds an item to the front of a deque."""

		self.items.append(item)

	def add_rear(self, item):
		"""Adds an item to the rear of a deque."""

		self.items.insert(0, item)

	def remove_front(self):
		"""Removes and returns an item from the front of a deque."""

		return self.items.pop()

	def remove_rear(self):
		"""Removes and returns an item from the rear of a deque."""

		return self.items.pop(0)

	def is_empty(self):
		"""Checks whether the deque is empty."""

		return self.items == []

	def size(self):
		"""Returns the number of items in the deque."""

		return len(self.items)

# Palindrome-Checker

def palindrome_check(word):
	"""Checks whether a given word is a palindrome.
	   Implemented using the deque ADT."""

	d = Deque()
	for c in word:
		d.add_front(c)

	palindrome = True

	while d.size() > 1 and palindrome:
		end = d.remove_rear()
		start = d.remove_front()
		if start != end:
			palindrome = False

	return palindrome

print palindrome_check('coolbeanssnaeblooc')
