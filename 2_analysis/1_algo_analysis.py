# listing 1
import time

def sumOfN2(n):
	"""Returns the sum of numbers from 1 to n and the running time."""

	start = time.time()

	theSum = 0
	for i in range(1, n + 1):
		theSum += i

	end = time.time()

	return theSum, end - start

# for i in range(5):
# 	print("Sum is %d required %10.7f seconds" % sumOfN2(1000000))

def sumOfN3(n):
	start = time.time()
	theSum = (n * (n + 1)) / 2
	end = time.time()

	return theSum, end - start

# for i in range(5):
# 	print("Sum is %d required %10.7f seconds" % sumOfN3(10000000000))

# Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. O(n2). The second function should be linear O(n).

def smallestNum(numList):
	"""Finds the smallest number in a list in O(n^2) time."""

	start = time.time()

	for i in numList:
		count = 0
		for n in numList:
			if i < n:
				count += 1
			if count == len(numList) - 1:
				end = time.time()
				return i, end - start

numList = [i for i in range(100000000)]
print 'The smallest num is %s, it took %10.7f seconds.' % (smallestNum(numList))

def smallestNum2(numList):
	"""Finds the smallest number in a list in O(n) time."""

	start = time.time()

	smallestNum = numList[0]
	for i in numList:
		if i < smallestNum:
			smallestNum = i
	end = time.time()
	return smallestNum, end - start

print 'The smallest num is %s, it took %10.7f seconds.' % (smallestNum2(numList))