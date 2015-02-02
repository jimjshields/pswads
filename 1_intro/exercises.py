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

# 3. Implement the remaining simple arithmetic operators (__sub__, __mul__, and __truediv__).

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

	def __sub__(self, other):
		"""Overrides the subtraction operator to subtract one fraction from another."""

		newNum = (self.num * other.denom) - (other.num * self.denom)
		newDenom = self.denom * other.denom
		return Fraction(newNum, newDenom)

	def __mul__(self, other):
		"""Overrides the multiplication operator to multiply two fractions together."""

		newNum = self.num * other.num
		newDenom = self.denom * other.denom
		return Fraction(newNum, newDenom)

	def __div__(self, other):
		"""Overrides the division operator to divide one fraction from another."""

		newNum = self.num * other.denom
		newDenom = self.denom * other.num
		return Fraction(newNum, newDenom)	

	def __str__(self):
		"""Overrides the string representation of a fraction object."""

		return "%s/%s" % (self.num, self.denom)

# fract1 = Fraction(1, 2)
# fract2 = Fraction(1, 4)

# print 'fract1 should be 1/2, fract2 should be 1/4'
# print 'fract1: %s, fract2: %s' % (fract1, fract2)
# print 'fract1 + fract2 should be 3/4'
# print 'fract1 + fract2 = %s' % (fract1 + fract2)
# print 'fract1 - fract2 should be 1/4'
# print 'fract1 - fract2 = %s' % (fract1 - fract2)
# print 'fract1 * fract2 should be 1/8'
# print 'fract1 * fract2 = %s' % (fract1 * fract2)
# print 'fract1 / fract2 should be 2/1'
# print 'fract1 / fract2 = %s' % (fract1 / fract2)

# 4. Implement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and __ne__)

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

	def commonDenom(self, other):
		"""Converts two fractions to the same denominator for comparison."""

		newDenom = self.denom * other.denom
		selfNum = (newDenom/self.denom) * self.num
		otherNum = (newDenom/other.denom) * other.num
		return selfNum, otherNum

	def __add__(self, other):
		"""Overrides the addition operator to add two fraction objects together."""

		newNum = (self.num * other.denom) + (other.num * self.denom)
		newDenom = self.denom * other.denom
		return Fraction(newNum, newDenom)

	def __sub__(self, other):
		"""Overrides the subtraction operator to subtract one fraction from another."""

		newNum = (self.num * other.denom) - (other.num * self.denom)
		newDenom = self.denom * other.denom
		return Fraction(newNum, newDenom)

	def __mul__(self, other):
		"""Overrides the multiplication operator to multiply two fractions together."""

		newNum = self.num * other.num
		newDenom = self.denom * other.denom
		return Fraction(newNum, newDenom)

	def __div__(self, other):
		"""Overrides the division operator to divide one fraction from another."""

		newNum = self.num * other.denom
		newDenom = self.denom * other.num
		return Fraction(newNum, newDenom)

	def __gt__(self, other):
		"""Overrides the > operator to compare two fractions and return a boolean."""

		selfNum, otherNum = self.commonDenom(other)
		return selfNum > otherNum

	def __ge__(self, other):
		"""Overrides the >= operator to compare two fractions and return a boolean."""

		selfNum, otherNum = self.commonDenom(other)
		return selfNum >= otherNum

	def __lt__(self, other):
		"""Overrides the < operator to compare two fractions and return a boolean."""

		selfNum, otherNum = self.commonDenom(other)
		return selfNum < otherNum

	def __le__(self, other):
		"""Overrides the <= operator to compare two fractions and return a boolean."""

		selfNum, otherNum = self.commonDenom(other)
		return selfNum <= otherNum

	def __ne__(self, other):
		"""Overrides the != operator to compare two fractions and return a boolean."""

		selfNum, otherNum = self.commonDenom(other)
		return selfNum != otherNum	

	def __str__(self):
		"""Overrides the string representation of a fraction object."""

		return "%s/%s" % (self.num, self.denom)

# fract1 = Fraction(1, 2)
# fract2 = Fraction(1, 4)

# print 'fract1 should be 1/2, fract2 should be 1/4'
# print 'fract1: %s, fract2: %s' % (fract1, fract2)
# print 'fract1 > fract2 should be True'
# print 'fract1 > fract2 = %s' % (fract1 > fract2)
# print 'fract1 < fract2 should be False'
# print 'fract1 < fract2 = %s' % (fract1 < fract2)
# print 'fract1 >= fract2 should be True'
# print 'fract1 >= fract2 = %s' % (fract1 >= fract2)
# print 'fract1 <= fract2 should be False'
# print 'fract1 <= fract2 = %s' % (fract1 <= fract2)
# print 'fract1 != fract2 should be True'
# print 'fract1 != fract2 = %s' % (fract1 != fract2)

# 5. Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator are both integers. If either is not an integer the constructor should raise an exception.

class Fraction(object):
	"""Represents a fraction."""

	def __init__(self, num, denom):
		"""Initiates fraction object with a numerator and denominator,
		   and uses the greatest common denominator to reduce the fraction."""

		if type(num) is not int or type(denom) is not int:
			raise ValueError('Num and denom must be integers.')

		common = gcd(num, denom)
		self.num = num / common
		self.denom = denom / common

	def getNum(self):
		return self.num

	def getDenom(self):
		return self.denom

	def commonDenom(self, other):
		"""Converts two fractions to the same denominator for comparison."""

		newDenom = self.denom * other.denom
		selfNum = (newDenom/self.denom) * self.num
		otherNum = (newDenom/other.denom) * other.num
		return selfNum, otherNum

	def __add__(self, other):
		"""Overrides the addition operator to add two fraction objects together."""

		newNum = (self.num * other.denom) + (other.num * self.denom)
		newDenom = self.denom * other.denom
		return Fraction(newNum, newDenom)

	def __sub__(self, other):
		"""Overrides the subtraction operator to subtract one fraction from another."""

		newNum = (self.num * other.denom) - (other.num * self.denom)
		newDenom = self.denom * other.denom
		return Fraction(newNum, newDenom)

	def __mul__(self, other):
		"""Overrides the multiplication operator to multiply two fractions together."""

		newNum = self.num * other.num
		newDenom = self.denom * other.denom
		return Fraction(newNum, newDenom)

	def __div__(self, other):
		"""Overrides the division operator to divide one fraction from another."""

		newNum = self.num * other.denom
		newDenom = self.denom * other.num
		return Fraction(newNum, newDenom)

	def __gt__(self, other):
		"""Overrides the > operator to compare two fractions and return a boolean."""

		selfNum, otherNum = self.commonDenom(other)
		return selfNum > otherNum

	def __ge__(self, other):
		"""Overrides the >= operator to compare two fractions and return a boolean."""

		selfNum, otherNum = self.commonDenom(other)
		return selfNum >= otherNum

	def __lt__(self, other):
		"""Overrides the < operator to compare two fractions and return a boolean."""

		selfNum, otherNum = self.commonDenom(other)
		return selfNum < otherNum

	def __le__(self, other):
		"""Overrides the <= operator to compare two fractions and return a boolean."""

		selfNum, otherNum = self.commonDenom(other)
		return selfNum <= otherNum

	def __ne__(self, other):
		"""Overrides the != operator to compare two fractions and return a boolean."""

		selfNum, otherNum = self.commonDenom(other)
		return selfNum != otherNum	

	def __str__(self):
		"""Overrides the string representation of a fraction object."""

		return "%s/%s" % (self.num, self.denom)