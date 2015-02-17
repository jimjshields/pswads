def binary_search(a_list, item):
	"""Performs a binary search of a list and returns a bool for whether the
	   item is found."""

	first = 0
	last = len(a_list) - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last) // 2
		if a_list[midpoint] == item:
			return True
		else:
			if item < a_list[midpoint]:
				last = midpoint - (midpoint // 2)