# Implementing a Stack in Python

class Stack(object):
	"""Represents the stack ADT. Implemented using the Python list.
	   Left is the base, right is the top."""

	def __init__(self):
		"""Initializes an empty stack."""

		self.items = []

	def push(self, item):
		"""Adds an item to the top of the stack."""

		self.items.append(item)

	def pop(self):
		"""Removes and returns the item at the top of the stack."""

		return self.items.pop()

	def peek(self):
		"""Returns the item at the top of the stack."""

		return self.items[-1]

	def is_empty(self):
		"""Tests for whether the stack is empty."""

		return self.items == []

	def size(self):
		"""Returns the number of items in the stack."""

		return len(self.items)

# s = Stack()

# print s.is_empty()
# s.push(4)
# s.push('dog')
# print s.peek()
# s.push(True)
# print s.size()
# print s.is_empty()
# s.push(8.4)
# print s.pop()
# print s.pop()
# print s.size()

# Simple Balanced Parentheses
# Using stack to write algo for determining balance of parentheses.

def balan_paren(symbol_string):
	"""Checks whether a string of parentheses is balanced."""

	s = Stack()
	balanced = True
	index = 0
	while index < len(symbol_string) and balanced:
		symbol = symbol_string[index]
		
		# Open parentheses go on top of the stack.
		if symbol == '(':
			s.push(symbol)

		# For any non-open parentheses, first check if the stack is empty.
		else:
			if s.is_empty():
				balanced = False
			# If not, get rid of the top open parentheses.
			else:
				s.pop()
		index += 1

	if balanced and s.is_empty():
		return True
	else:
		return False

symbol_string = '(((())(())))'
# print balan_paren(symbol_string)

# Balanced Symbols (A General Case)
# Using a stack to write algo for determining balance of symbols.

def balan_symbol(symbol_string):
	"""Checks whether a string of symbols is balanced."""

	s = Stack()
	balanced = True
	index = 0

	while index < len(symbol_string) and balanced:
		symbol = symbol_string[index]
		if symbol in '{[(<':
			s.push(symbol)

		else:
			if s.is_empty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False

		index += 1

	if balanced and s.is_empty():
		return True
	else:
		return False

def matches(open_sym, close_sym):
	"""Checks whether the opening symbol matches the closing symbol, returns a boolean."""

	open_symbols = '{[(<'
	close_symbols = '}])>'

	return open_symbols.index(open_sym) == close_symbols.index(close_sym)

# print balan_symbol('{[()]}')
# print balan_symbol('{([)]}')
# print balan_symbol('((([[[{{{<>}}}]]])))')

# Converting Decimal Numbers to Binary Numbers

# Implementing a 'divide by 2' algo for conversion

def divide_by_2(base_10_int):
	"""Returns a base 2 representation (string) of a base 10 number (integer)."""

	rem_stack = Stack()

	while base_10_int > 0:
		rem = base_10_int % 2
		rem_stack.push(rem)
		base_10_int = base_10_int // 2

	bin_string = ''

	while not rem_stack.is_empty():
		bin_string += str(rem_stack.pop())

	return bin_string

# print divide_by_2(324423324432432)

# Generalized base conversion

def base_converter(base_10_int, to_base):
	"""Returns a to_base base repr (str) of a base 10 num (int)."""

	DIGITS = '0123456789ABCDEF'

	rem_stack = Stack()

	while base_10_int > 0:
		rem = base_10_int % to_base
		rem_stack.push(rem)
		base_10_int = base_10_int // to_base

	to_base_string = ''

	while not rem_stack.is_empty():
		to_base_string += DIGITS[rem_stack.pop()]

	return to_base_string

# print base_converter(25, 2)
# print base_converter(256, 16)

# Infix, Prefix, and Postfix Expressions

def infix_to_postfix(infix_expr):
	"""Converts an infix expression to a postfix expression."""

	precedence = {}
	precedence['*'] = 3
	precedence['/'] = 3
	precedence['+'] = 2
	precedence['-'] = 2
	precedence['('] = 1
	
	operator_stack = Stack()
	postfix_list = []
	token_list = infix_expr.split()

	for token in token_list:
		# print token
		if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
			postfix_list.append(token)
		elif token == '(':
			operator_stack.push(token)
		elif token == ')':
			top_token = operator_stack.pop()
			while top_token != ')':
				postfix_list.append(top_token)
				top_token = operator_stack.pop()

		else:
			while (not operator_stack.is_empty()) and (precedence[operator_stack.peek()] >= precedence[token]):
				postfix_list.append(operator_stack.pop())
			operator_stack.push(token)

	while not operator_stack.is_empty():
		postfix_list.append(operator_stack.pop())
	return ' '.join(postfix_list)

print infix_to_postfix('A * B + C * D')
print infix_to_postfix('( A + B ) * ( C + D )') # bug here? Not sure what.

# skipping the last problem; not very helpful.