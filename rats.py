targets = dict() # map[set()]int
as_found = []

for original in range(10_000):
	def rats(x: int):
		r = int(str(x)[::-1])
		s = x + r
		return int(''.join(sorted(str(s))))

	def convert(x: set):
		return ' '.join(list(map(str, x)))
	
	def make_set(x: str) -> set:
		return set(list(map(int, x.split(' '))))

	found = set()

	while_t = True

	r = original
	while while_t:
		found.add(r)
		r = rats(r)

		if r >= 10 ** 12:
			break

		for target_repr in targets.keys():
			target_set = make_set(target_repr)
			if r in target_set:
				count = targets[target_repr]
				del targets[target_repr]
				target_set = target_set.union(found)

				new_repr = convert(target_set)
				if target_repr in as_found:
					as_found[as_found.index(target_repr)] = new_repr
				targets[new_repr] = count + 1
				while_t = False
				break
		else:
			found_repr = convert(found)
			targets[found_repr] = 1
			as_found.append(found_repr)

for found in as_found:
	components = list(map(int, found.split(' ')))
	components.sort()

	if len(components) < 2:
		continue

	print(f'Period: {len(components)}, occurs {targets[found]} times, cycle: {' '.join(map(str, components))}')
