amount = int(input())

def iso_pattern(word1):
	code = [0] * len(word1)

	for idx1, ch1 in enumerate(word1):
		for nidx1, nch1 in enumerate(word1):
			if nidx1 <= idx1:
				continue
	
			if ch1 == nch1 and code[idx1] == 0:
				code[idx1] = nidx1 - idx1

	return code

def iso(word1, word2):
	code1 = iso_pattern(word1)
	code2 = iso_pattern(word2)

	if code1 != code2:
		return None

	def f(i: int):
		if i > 0:
			return f'+{i}'
		return '0'

	return ' '.join(map(f, code1))

for _ in range(amount):
	line = input().split()
	word1 = line[0]
	word2 = line[1]

	if len(word1) != len(word2):
		print(f'{word1}, {word2} have different lengths')
		continue

	if k := iso(word1, word2):
		print(f'{word1}, {word2} are isomorphs with repetition pattern {k}')
	else:
		print(f'{word1}, {word2} are not isomorphs')