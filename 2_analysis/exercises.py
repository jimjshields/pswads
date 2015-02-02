# 1. Devise an experiment to verify that the list index operator is O(1)

import timeit
import random

for i in range(100001, 10000001, 200000):
	t = timeit.Timer('x[random.randrange(%d)]' % (i), 'from __main__ import random, x')
	x = list(range(i))
	list_time = t.timeit(number=1000)

	print '%d, %10.3f' % (i, list_time)

# 2. Devise an experiment to verify that get item and set item are O(1) for dictionaries.

for i in range(100001, 10000001, 200000):
	t = timeit.Timer('x[random.randrange(%d)]' % (i), 'from __main__ import random, x')
	x = {j:None for j in range(i)}

	set_time = t.timeit(number=1000)

	x = [x[j] for j in range(i)]

	get_time = t.timeit(number=1000)

	print '%d, %10.3f, %10.3f' % (i, set_time, get_time)

# 3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.

# solution here

# 4. Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.

def smallestNumber(numList, k):
	"""Returns the kth smallest number in a list of randomly-sorted numbers.
	   Operates in nlog(n) time."""

	# O(nlog(n))
	numList.sort()

	# O(1)
	return numList[k - 1]

# 5. Can you improve the algorithm from the previous problem to be linear? Explain.

# No - since sorting generally takes O(nlog(n)), and you need sorting. Unless there's a way to get that number w/o sorting.
