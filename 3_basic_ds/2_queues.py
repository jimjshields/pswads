# The Queue Abstract Data Type
# Implementing a Queue in Python

class Queue(object):
	"""Represents a Queue ADT."""

	def __init__(self):
		"""Initializes an empty queue."""

		self.items = []

	def enqueue(self, item):
		"""Adds an item to the end/rear of the queue."""

		self.items.append(item)

	def dequeue(self):
		"""Removes an item from front of the queue."""

		return self.items.pop(0)

	def is_empty(self):
		"""Checks if the queue is empty; returns a boolean."""

		return self.items == []

	def size(self):
		"""Returns the number of items in the queue."""

		return len(self.items)

# q = Queue()
# print q.is_empty()
# q.enqueue(4)
# q.enqueue('dog')
# q.enqueue(True)
# print q.size()
# print q.is_empty()
# q.enqueue(8.4)
# print q.dequeue()
# print q.dequeue()
# print q.size()
# print q.items

# Simulation: Hot Potato

def hot_potato(name_list, num):
	"""Takes a list of names and number of passes in a simulated game of hot potato.
	   Returns the simulated winner of the game."""

	sim_queue = Queue()
	for name in name_list:
		sim_queue.enqueue(name)

	while sim_queue.size() > 1:
		for i in range(num):
			sim_queue.enqueue(sim_queue.dequeue())

		sim_queue.dequeue()

	return sim_queue.dequeue()

# print hot_potato(['Bill', 'Dave', 'Jim', 'Nora'], 4)

# Simulation: Printing Tasks

class Printer(object):
	"""Represents a printer."""

	def __init__(self, page_rate):
		self.page_rate = page_rate
		self.current_task = None
		self.time_remaining = 0

	def tick(self):
		if self.current_task != None:
			self.time_remaining = self.time_remaining - 1
			if self.time_remaining <= 0:
				self.current_task = None

	def busy(self):
		if self.current_task != None:
			return True
		else:
			return False

	def start_next(self, new_task):
		self.current_task = new_task
		self.time_remaining = new_task.get_pages() * (60/self.page_rate)

import random

class Task(object):
	"""Represents a printer task."""

	def __init__(self, time):
		self.timestamp = time

		# Initialize task pages as a random number b/w 1 and 20.
		self.pages = random.randrange(1, 21)

	def get_stamp(self):
		return self.timestamp

	def get_pages(self):
		return self.pages

	def wait_time(self, current_time):
		return current_time - self.timestamp

def simulation(num_secs, page_rate):
	"""Simulates a printer queue for a given number of seconds and page rate."""

	lab_printer = Printer(page_rate)
	print_queue = Queue()
	waiting_times = []

	for current_second in range(num_secs):
		if new_print_task():
			task = Task(current_second)
			print_queue.enqueue(task)

		if (not lab_printer.busy()) and (not print_queue.is_empty()):
			next_task = print_queue.dequeue()
			waiting_times.append(next_task.wait_time(current_second))
			lab_printer.start_next(next_task)

		lab_printer.tick()

	average_wait = sum(waiting_times)/len(waiting_times)
	print 'Average wait: %6.2f seconds %3d tasks remaining.' % (average_wait, print_queue.size())

def new_print_task():
	num = random.randrange(1, 181)
	if num == 180:
		return True
	else:
		return False

for i in range(10):
	simulation(3600, 5)

