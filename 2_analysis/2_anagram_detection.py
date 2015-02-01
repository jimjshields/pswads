import time

# Solution 1: Checking Off

def anagramSolution(word1, word2):
	"""Returns a boolean - True if word1 and word2 are anagrams of each other.
	   This is of O(n^2) complexity."""

	start = time.time()

	aList = list(word2)

	pos1 = 0
	stillOk = True

	while pos1 < len(word1) and stillOk:
		pos2 = 0
		found = False
		while pos2 < len(aList) and not found:
			if word1[pos1] == aList[pos2]:
				found = True
			else:
				pos2 += 1

		if found:
			aList[pos2] = None
		else:
			stillOk = False

		pos1 += 1

	end = time.time()
	
	return stillOk, end - start

# Solution 2: Sort and Compare

def anagramSolution2(word1, word2):
	"""Returns a boolean - True if word1 and word2 are anagrams of each other.
	   This has the complexity of the sorts (generally O(nlog(n)))."""

	start = time.time()

	aList1 = list(word1)
	aList2 = list(word2)

	aList1.sort()
	aList2.sort()

	pos = 0
	matches = True

	while pos < len(word1) and matches:
		if aList1[pos] == aList2[pos]:
			pos += 1
		else:
			matches = False

	end = time.time()
	
	return matches, end - start

# Solution 3: Brute Force

# Just don't even try - there are n! # of permutations to run through

# Solution 4: Count and Compare

def anagramSolution4(word1, word2):
	"""Returns a boolean - True if word1 and word2 are anagrams of each other.
	   This is implemented using two lists of counters for all alpha characters.
	   This has O(n) complexity.
	   Importantly, this also takes more space - tradeoff."""

	start = time.time()

	c1 = [0] * 26
	c2 = [0] * 26

	for i in range(len(word1)):

		pos = ord(word1[i]) - ord('a')
		c1[pos] += 1

	for i in range(len(word2)):
		pos = ord(word2[i]) - ord('a')
		c2[pos] += 1

	j = 0
	stillOk = True
	while j < 26 and stillOk:
		if c1[j] == c2[j]:
			j += 1
		else:
			stillOk = False

	end = time.time()

	return stillOk, end - start