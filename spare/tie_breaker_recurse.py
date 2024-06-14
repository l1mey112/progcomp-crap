n = 4
s = 66
r = 1.58334


def find_sum_sets(n, s):
	# Indicates we've run out of number slots
	if n == 0:
		if s == 0:
			# Valid solution, so we return an empty list
			# (which will later have the rest of the chain added to it)
			return [[]]
		else:
			return []
	if s < 0:
		return []

	sets = []
	for i in range(s):
		# Recurse
		subsets = find_sum_sets(n - 1, s - (i + 1))

		for subset in subsets:
			# Check for duplicates
			if (i + 1) in subset:
				continue

			# Ensure first item in list is the smallest, otherwise throw out list
			if len(subset):
				if (i + 1) > subset[0]:
					continue

			sets.append([i + 1] + subset)
	return sets


# Returns True if a sum is found
def search_for_sums(candidate):
	sums = []
	for i in candidate:
		# If the number is found in the list of sums we've found
		if i in sums:
			return True

		# If a combination of this number and any of the sums already exists,
		# throw it away. Then add all the current sums plus our number
		sums_to_add = []
		for sum in sums:
			if sum + i in sums:
				return True
			else:
				sums_to_add.append(sum + i)
		sums.extend(sums_to_add)

		sums.append(i)
		# sums.extend([x + i for x in sums])

	return False


def main():
	candidates = find_sum_sets(n, s)
	result = []

	for candidate in candidates:
		# Checking for ratio between first and last
		if candidate[-1] / candidate[0] > r:
			continue

		if search_for_sums(candidate):
			continue

		result.append(candidate)

	for list in result:
		print(" ".join(map(str, list)))


if __name__ == "__main__":
	main()
