amount = int(input())

def reduce(v: int, year: bool = False):
	if not year and v % 11 == 0:
		return v
	
	acc = 0
	
	for ch in str(v):
		digit = int(ch)
		acc += digit

	if not year and acc % 11 == 0:
		return acc

	if len(str(acc)) > 1:
		acc = reduce(acc)

	return acc

for _ in range(amount):
	line = input()
	com = list(map(int, line.split('/')))

	acc = 0

	acc += reduce(com[0]) # day
	acc += reduce(com[1]) # month
	acc += reduce(com[2], True) # year

	if acc % 11 == 0:
		# master
		pass
	elif len(str(acc)) == 2:
		acc = reduce(acc)

	print(f'{acc} {line}')
