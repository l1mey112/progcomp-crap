import fileinput

def main(line: str):
	pos = 0
	top = True
	direction = 'V' # V C A

	def topline() -> str:
		return f'V{pos} {"T" if top else "B"} {direction}'

	print(topline())

	def enact(c: str):
		nonlocal pos
		nonlocal top
		nonlocal direction
		
		if direction == 'V':
			if c == 'L':
				pos += 1
				direction = 'C'
			else:
				pos -= 1
				direction = 'A'
		elif direction == 'C':
			if top:
				if c == 'L':
					top = not top
					direction = 'V'
					if pos == 1:
						pos = 3
					elif pos == 3:
						pos = 1
				else:
					pos += 1
					direction = 'C'
			else:
				if c == 'R':
					top = not top
					direction = 'V'
					if pos == 1:
						pos = 3
					elif pos == 3:
						pos = 1
				else:
					pos += 1
					direction = 'C'
		elif direction == 'A':
			if top:
				if c == 'L':
					pos -= 1
					direction = 'A'
				else:
					top = not top
					direction = 'V'
					if pos == 1:
						pos = 3
					elif pos == 3:
						pos = 1
			else:
				if c == 'R':
					pos -= 1
					direction = 'A'
				else:
					top = not top
					direction = 'V'
					if pos == 1:
						pos = 3
					elif pos == 3:
						pos = 1

		pos = pos % 4

		print(f'{c} -> {topline()}')

	for c in line:
		enact(c)

	# quickest

	print('home')

	if pos == 0 and top:
		return

	if not top:
		if direction == 'V':
			if pos in [1, 2]:
				enact('L')
			else:
				enact('R')

	if direction == 'C':
		enact('R')
	else:
		enact('L')

	while not (pos == 0 and top):
		if direction == 'C':
			enact('R')
		elif direction == 'A':
			enact('L')
		else:
			if pos in [1, 2]:
				enact('L')
			else:
				enact('R')

i = 1
for line in fileinput.input():
	print(f'ant #{i}')
	main(line.strip())
	print()
	i += 1
