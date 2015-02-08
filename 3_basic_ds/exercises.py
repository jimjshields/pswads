# Chapter 3 Programming Exercises
# Skip all pre-/post-/infix questions; not worth the time.
# Also skip any 'experiment' questions. Maybe come back to them.

# 5. Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.

class Queue(object):
	"""Represents a queue ADT. The rear of the queue is the end of the list used.
	   Necessary methods: enqueue, dequeue, size, is_empty."""

	def __init__(self):
		"""Initializes an empty queue using a list."""

		self.items = []

	def enqueue(self, item):
		"""Adds an item to the rear of the queue."""

		self.items.append(item)

	def dequeue(self):
		"""Removes and returns an item from the front of the queue."""

		return self.items.pop(0)

	def size(self):
		"""Returns the number of items in the queue."""

		return len(self.items)

	def is_empty(self):
		"""Checks whether the queue has no items."""

		return self.items == []

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# print q.items
# print q.dequeue()
# print q.dequeue()
# print q.dequeue()
# print q.dequeue()
# print q.dequeue()
# print q.is_empty()

# 7. It is possible to implement a queue such that both enqueue and dequeue have O(1) performance on average. In this case it means that most of the time enqueue and dequeue will be O(1) except in one particular circumstance where dequeue will be O(n).

class Queue_2(object):
	"""Represents a queue ADT with O(1) enqueue and dequeue time on average."""

	def __init__(self):
		"""Initializes an empty queue with a list.
		   Also initializes the dequeue variable for O(1) access time."""

		self.items = []
		self.to_be_dequeued = ''

	def enqueue(self, item):
		self.items.append(item)
		self.to_be_dequeued = self.items[0]

