# Implementing an Unordered List: Linked Lists

class Node(object):
	"""Represents a node in an unordered list."""

	def __init__(self, init_data):
		"""Initializes with its data and a placeholder for the next node."""

		self.data = init_data
		self.next = None

	def get_data(self):
		"""Accessor for a node's data."""

		return self.data

	def get_next(self):
		"""Accessor for the next node."""

		return self.next

	def set_data(self, new_data):
		"""Setter for the node's data."""

		self.data = new_data

	def set_next(self, new_next):
		"""Setter for the reference to the next node."""

		self.next = new_next

n = Node(10)

class UnorderedList(object):
	"""Represents an unordered list ADT."""

	def __init__(self):
		"""Initializes unordered list with an empty head reference."""

		self.head = None

	def get_head(self):
		"""Accessor for the reference to the head node."""

		return self.head

	def add_item(self, item):
		"""Setter for the reference to the head node.
		   Sets the head to the new node, and the next
		   node of the new node to the old head."""

		temp = Node(item)
		temp.set_next(self.head)
		self.head = temp

	def is_empty(self):
		"""Checks if an unordered list is empty."""

		return self.head == None

	def size(self):
		"""Returns the number of items in the unordered list."""

		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.get_next()
		
		return count

	def search(self, item):
		"""Attempts to find an item in an unordered list."""

		current = self.head
		found = False

		while current != None and not found:
			if current.get_data() == item:
				found = True
			else:
				current = current.get_next()

		return found

	def remove(self, item):
		"""Removes an item from an unordered list."""

		current = self.head
		previous = None
		found = False

		while not found:
			if current.get_data() == item:
				found = True
			else:
				previous = current
				current = current.get_next()

		if previous == None:
			self.head = current.get_next()	
		else:
			previous.set_next(current.get_next())

	def append(self, item):
		"""Appends an item to the end of an unordered list."""

		current = self.head

		while current.get_next() != None:
			current = current.get_next()

		current.set_next(Node(item))

	def insert(self, index, item):
		"""Inserts an item at a given index in an unordered list."""

		current = self.head
		previous = None
		current_index = 0

		while current != None and current_index != index:
			current_index += 1
			previous = current
			current = current.get_next()

		if index != current_index:
			print "%s is not an index in this list." % (index)
		elif index == 0:
			new_node = Node(item)
			old_node = self.get_head()
			self.head = new_node
			new_node.set_next(old_node)
		else:
			new_node = Node(item)
			old_node = current
			previous.set_next(new_node)
			new_node.set_next(old_node)

	def index(self, item):
		"""Returns the index of the given item."""

		if not self.search(item):
			print "This item isn't in the list."
		else:
			current = self.head
			current_index = 0
			while current.get_data() != item:
				current_index += 1
				current = current.get_next()
			return current_index

	def pop(self, index=0):
		"""Removes the node at the given index and returns it."""

		

u = UnorderedList()
u.add_item(10)
u.add_item(15)
u.add_item(16)
u.add_item(20)
u.add_item(1)
u.add_item(-100)
u.append(500)
u.insert(4, 'hello')

current = u.get_head()
while current != None:
	print current.get_data()
	current = current.get_next()

print u.index('hello')
# print u.search(20)

# u.remove(-100)
# u.remove(20)
# current = u.get_head()
# while current != None:
# 	print current.get_data()
# 	current = current.get_next()