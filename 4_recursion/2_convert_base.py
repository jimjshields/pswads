def convert_base(num, to_base):
	"""Converts a positive integer to a string of a given base."""

	digits = '0123456789ABCDEF'

	if num < to_base:
		return str(num)
	else:
		return convert_base(num // to_base, to_base) + digits[num % to_base]

# print convert_base(10, 2) == '1010'
# print convert_base(1, 2) == '1'
# print convert_base(0, 2) == '0'
# print convert_base(10, 10) == '10'
# print convert_base(16, 16) == '10'
# print convert_base(10, 2)
# print convert_base(1, 2)
# print convert_base(42, 16)

# Self check

# Recursively return the reverse of a string

def reverse_string_rec(string):
	"""Return the recursively-calculated reverse of a string."""

	if len(string) == 1:
		return string
	else:
		return reverse_string_rec(string[1:]) + string[0]

# print reverse_string_rec('hello')
# print reverse_string_rec('hello') == 'olleh'
# print reverse_string_rec('racecar') == reverse_string_rec('racecar')
# print reverse_string_rec('a') == 'a'

# Recursively check if palindrome

def is_palindrome_rec(string):
	"""Recursively checks whether a string is a palindrome."""

	if string == '':
		return True
	elif len(string) == 1:
		return True
	else:
		if string[0] == string[-1]:
			return is_palindrome_rec(string[1:-1])
		else:
			return False

print is_palindrome_rec('racecar')
print is_palindrome_rec('a')
print is_palindrome_rec('')
print is_palindrome_rec('hello')