import regex

def is_trivial(s: str):
	if len(s) <= 2:
		return True

	return s in ["for", "has", "have", "she", "that", "the", "this", "will", "with"]

def is_vowel(s: str):
	return regex.match(r'[aeiou]', s) != None

amount = int(input())

for _ in range(amount):
	line = input()
	words = line.split(' ')

	prefixes = []
	endings = []
	prefix_idx_of_swap = []

	for idx, word in enumerate(words):
		if is_trivial(word) or is_vowel(word):
			prefixes.append('')
			endings.append(word)
			continue

		extract = regex.match(r'[^aeiou]+', word)
		prefix, lasting = extract[0], word.removeprefix(extract[0])

		if prefix == 'q' and lasting[0] == 'u':
			prefix += 'u'
			lasting = lasting[1:]

		prefixes.append(prefix)
		endings.append(lasting)
		prefix_idx_of_swap.append(idx)

	new_words = []

	for idx, prefix in enumerate(prefixes):
		if idx in prefix_idx_of_swap:
			prefix_idx = prefix_idx_of_swap.index(idx)
			prefix_idx = (prefix_idx - 1) % len(prefix_idx_of_swap)
			nidx = prefix_idx_of_swap[prefix_idx]

			new_words.append(prefixes[nidx] + endings[idx])
		else:
			new_words.append(words[idx])

	print(" ".join(new_words))
