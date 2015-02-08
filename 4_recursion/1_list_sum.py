def list_sum(num_list):
	"""Returns the recursively-calculated sum of a list of numbers."""

	if len(num_list) == 1:
		return num_list[0]
	else:
		return num_list[0] + list_sum(num_list[1:])

print list_sum([1, 2, 3, 4, 5, 10])