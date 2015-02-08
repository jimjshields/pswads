# Implementing an Ordered List

class OrderedList(object):
	"""Represents an ordered list, i.e., a collection of items in which
	   each item holds a position relative to the other items, where that
	   position is based on some underlying characteristic. 
	   e.g., integers in ascending order.

	   Assumes that there is a meaningful comparison operator defined 
	   for the items."""

	def __init__(self):
		"""Initializes an empty ordered list by specifying a pointer
		   to an empty head node."""

		self.head = None

	def get_head(self):
		"""Accessor for the head of the list."""

		return self.head

	def is_empty(self):
		"""Boolean for whether the ordered list is empty."""

		return self.head == None

	def size(self):
		"""Returns the number of items in the ordered list."""

		current = self.get_head()
		count = 0

		while current != None:
			count += 1
			current = current.get_next()

		return count

	def search(self, item):
		"""Searches the list for a given item.
		   Returns True if found, False if not."""

		current = self.head
		found = False
		stop = False

		while current != None and not found and not stop:
			if current.get_data() == item:
				found = True
			elif current.get_data() > item:
				stop = True
			else:
				current = current.get_next()

		return found

	def add_item(self, item):
		"""Adds an item to the ordered list in its proper position."""

		current = self.head
		previous = None
		stop = False

		while current != None and not stop:
			if current.get_data() > item:
				stop = True
			else:
				previous = current
				current = current.get_next()

		temp = Node(item)
		if previous != None:
			temp.set_next(current)
			previous.set_next(temp)
		else:
			temp.set_next(self.head)
			self.head = temp

	def remove_item(self, item):
		"""Removes a given item from the list and returns it if found."""

		current = self.head
		found = False
		stop = False

		while not found and not stop:
			if current.get_data() > item:
				stop = True
			elif current.get_data() == item:
				found = True
			else:
				previous = current
				current = current.get_next()

		if found:
			next = current.get_next()
			if previous != None:
				previous.set_next(current.get_next())
				return current.get_data()
			else:
				self.head = next
				return current.get_data()
		else:
			return False

	def index(self, item):
		"""Returns the index of a given item."""

		current = self.head
		current_index = 0

		if not self.search(item):
			return False

		while current.get_data() != item:
			current_index += 1
			current = current.get_next()

		return current_index

	def pop(self, index=0):
		"""Removes the node at a given index and returns it."""

		current = self.head
		previous = None
		current_index = 0

		if index > self.size() - 1:
			return False
		else:
			while current != None and current_index != index:
				current_index += 1
				previous = current
				current = current.get_next()

		if previous != None:
			previous.set_next(current.get_next())
		else:
			self.head = current.get_next()
		return current.get_data()


class Node(object):
	"""Represents a node object. Can be placed in a linked list."""

	def __init__(self, data):
		"""Initializes a node object with given data and a pointer 
		   to an empty next node."""

		self.data = data
		self.next = None

	def get_next(self):
		"""Accessor for the next node."""

		return self.next

	def set_next(self, new_next):
		"""Setter for the pointer to the next node."""

		self.next = new_next

	def get_data(self):
		"""Accessor for the node's data."""

		return self.data

	def set_data(self, new_data):
		"""Setter for the node's data."""

		self.data = new_data

ol = OrderedList()
print ol.get_head()
ol.add_item(1)
ol.add_item(2)
ol.add_item(3)
ol.add_item(4)
ol.add_item(3)
ol.add_item(-100)
ol.add_item(-1)
print ol.pop()
print ol.pop(5)
current = ol.get_head()
while current != None:
	print current.get_data()
	current = current.get_next()