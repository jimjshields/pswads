def gcd(m, n):
	"""Returns the greatest common denominator of m and n."""

	if m > n:
		big = m
		small = n
	else:
		big = m
		small = n
	if big % small == 0:
		return small
	else:
		return gcd(small, big % small)

class Fraction(object):
	"""Represents a fraction."""
	def __init__(self, num, denom):
		self.num = num
		self.denom = denom

	def __str__(self):
		return "%s / %s" % (self.num, self.denom)

	def __add__(self, other):
		common = gcd(self.denom, other.denom)
		newNum = ((self.num * other.denom) + (other.num * self.denom))/common
		newDenom = (self.denom * other.denom)/common
		return Fraction(newNum, newDenom)

	def __eq__(self, other):
		firstNum = self.num * other.denom
		secondNum = other.num * self.denom
		return firstNum == secondNum

myFraction = Fraction(1, 2)
print "MyFraction = %s" % (myFraction)

otherFraction = Fraction(1, 4)
print "%s + %s = %s" % (myFraction, otherFraction, myFraction + otherFraction)

newFraction = Fraction(50, 100)
print "%s is %s to %s" % (myFraction, "equal" if myFraction == newFraction else "not equal", newFraction)