# dynamic programming - often used for optimization problems

# Counting change problem - multiple approaches

# Easiest - greedy
# Harder and guaranteed to work - recursion

def make_change(change, coins_list):
	"""Returns the smallest num of coins to make a given amt of change."""

	min_coins = change

	if change in coins_list:
		return 1
	else:
		for i in [c for c in coins_list if c <= change]:
			num_coins = 1 + make_change(change - i, coins_list)
			if num_coins < min_coins:
				min_coins = num_coins
	return min_coins

def make_change_2(change, coins_list, known_results):
	"""Returns the smallest num of coins to make a given amt of change.
	   Memoizes/caches calculations to cut down on function calls."""

	min_coins = change

	# If it's one of the coins, that's the minimum
	if change in coins_list:
		# Add it to known results
		known_results[change] = 1
		return 1

	# If it's already been calculated, just return it
	elif known_results[change] > 0:
		return known_results[change]

	# Otherwise, calculate it
	else:
		for i in [c for c in coins_list if c <= min_coins]:
			num_coins = 1 + make_change_2(change - i, coins_list, known_results)

			# If the number of coins for a given amt of change is less
			# than the least ever, make that the min and add it to the
			# known results
			if num_coins < min_coins:
				min_coins = num_coins
				known_results[change] = min_coins

	return min_coins

# print make_change_2(63, [1, 5, 10, 25], [0] * 64)

def make_change_dynamic(change, coins_list, min_coins, coins_used):
	"""Returns the smallest num of coins to make a given amt of change.
	   Does this dynamically by incrementally calculating the minimum."""

	for i in xrange(1, change + 1):
		# Start by assuming the worst - takes i coins to make i change.
		coin_count = i

		# For all of the coins up to i
		for j in [c for c in coins_list if c <= i]:

			# If we've already calculated a minimum, just access that
			if min_coins[i - j] + 1 < coin_count:
				coin_count = min_coins[i - j] + 1
			min_coins[i] = coin_count
			
	return min_coins[change]

print make_change_dynamic(33, [1, 5, 8, 10, 25], [0] * 34, [0] * 34)