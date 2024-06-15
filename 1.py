import fileinput

def is_newline(s: str):
	return s.endswith('.') or s.endswith('!') or s.endswith('?')

words = []
for line in fileinput.input():
	words.extend(filter(lambda x: x != '', line.strip().split(' ')))

new_order = []
search_words = words.copy()
while len(search_words) > 0:
	hit = []

	i = 0
	n = 0
	while True:
		nnext = i + n

		if nnext >= len(search_words):
			break

		hit.append(nnext)
		
		i += n
		n += 1

	nsearch_words = []

	for idx, v in enumerate(search_words):
		if idx in hit:
			new_order.append(v)
		else:
			nsearch_words.append(v)

	search_words = nsearch_words

for word in new_order:
	print(word, end=' ')
	if is_newline(word):
		print()

print()