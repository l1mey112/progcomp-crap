import regex

count = int(input())

consonants = ''

def plural(s: str):
	if s.endswith('s') or s.endswith('x') or s.endswith('z') or s.endswith('ch') or s.endswith('sh'):
		s += 'es'
	elif regex.match(r'\S+[bcdfghjklmnpqrstvwxz]o$', s):
		s += 'es'
	elif regex.match(r'\S+[bcdfghjklmnpqrstvwxz]y$', s):
		s = s.removesuffix('y')
		s += 'ies'
	elif regex.match(r'\S+[^f]fe$', s):
		s = s.removesuffix('fe')
		s += 'ves'
	elif regex.match(r'\S+[^f]f$', s):
		s = s.removesuffix('f')
		s += 'ves'
	else:
		s += 's'

	return s

for _ in range(count):
	line = input().split(' ')
	count = int(line[0])
	word = line[1]

	if count == 0:
		word = plural(word)
		Q = 'no'
	elif count == 1:
		Q = 'one'
	else:
		word = plural(word)
		Q = str(count)

	print(Q, word)