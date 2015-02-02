# 1. Implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction.
class Fraction(object):
	"""Represents a fraction."""

	def __init__(self, num, denom):
		"""Initiates fraction object with a numerator and denominator."""

		self.num = num
		self.denom = denom

	def getNum(self):
		return self.num

	def getDenom(self):
		return self.denom

# 2. In many ways it would be better if all fractions were maintained in lowest terms right from the start. Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.

def gcd(num, denom):
	"""Returns an integer of the greatest common denominator of two integers."""

	if num > denom:
		big = num
		small = denom
	else:
		big = denom
		small = num
	if big % small == 0:
		common = small
		return common
	else:
		return gcd(small, big % small)

class Fraction(object):
	"""Represents a fraction."""

	def __init__(self, num, denom):
		"""Initiates fraction object with a numerator and denominator,
		   and uses the greatest common denominator to reduce the fraction."""

		common = gcd(num, denom)
		self.num = num / common
		self.denom = denom / common

	def getNum(self):
		return self.num

	def getDenom(self):
		return self.denom

	def __add__(self, other):
		"""Overrides the addition operator to add two fraction objects together."""

		newNum = (self.num * other.denom) + (other.num * self.denom)
		newDenom = self.denom * other.denom
		return Fraction(newNum, newDenom)

	def __str__(self):
		"""Overrides the string representation of a fraction object."""

		return "%s / %s" % (self.num, self.denom)

# 3. 