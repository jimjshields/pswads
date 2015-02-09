# 1. Write a recursive function to compute the factorial of a number.

def factorial(n):
	"""Return the recursively-computed factorial of n."""

	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)

# 2. Write a recursive function to reverse a list.

def reverse_list(lst, reversed_list=[]):
	"""Returns a recursively-reversed list."""

	if len(lst) == 1:
		reversed_list.append(lst[0])
	else:
		reversed_list.append(lst[-1])
		reverse_list(lst[:-1])
	return reversed_list

print reverse_list([1, 2, 3, 4, 5, 1, 3])