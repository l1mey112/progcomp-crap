import regex

amount = int(input())

def l_type(line: str):
	letters = 'abcdefghijklmnopqrstuvwxyz'
	mark = None

	if line == '':
		return False

	for idx, l in enumerate(line):
		if not mark:
			idx_letter = letters.find(l)
			mark = idx_letter
		else:
			nidx_letter = letters.find(l)
			if mark > nidx_letter:
				return False
			mark = nidx_letter

	return True

def v_type(line: str):
	line = regex.sub(r'[^aeiou]', '', line)
	if line == '':
		return False

	letters = 'aeiou'
	mark = None

	for idx, l in enumerate(line):
		if not mark:
			idx_letter = letters.find(l)
			mark = idx_letter
		else:
			nidx_letter = letters.find(l)
			if mark > nidx_letter:
				return False
			mark = nidx_letter

	return True

for _ in range(amount):
	line = input()

	if l_type(line):
		print(f'L {line}')
	elif v_type(line):
		print(f'V {line}')
	else:
		print(f'N {line}')
