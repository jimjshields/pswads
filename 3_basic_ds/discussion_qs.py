# 1. Convert the following values to binary using "divide by 2." Show the stack of remainders.

def convert_to_base_2(num):
	"""Returns binary string repr of base 10 int."""

	if num == 0:
		return '0'
	elif num == 1:
		return '1'
	else:
		rem = num % 2
		num = num // 2
		bin_num = convert_to_base_2(num) + str(rem)
	return bin_num

print convert_to_base_2(17)
print convert_to_base_2(45)
print convert_to_base_2(96)

# other questions less programming-based.