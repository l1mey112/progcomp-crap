import math


lines = input().split(' ')
max_a, max_b = int(lines[0]), float(lines[1])

is_even = (max_b % 1.0 > 0 and max_b % 1.0 < 1)

print('_' * int(2 * (max_b * 2) + 1), end='')

print()

for i in range(max_a):
	max_top = math.floor(max_b)
	odd = (i + 1) % 2 == 0
	if odd:
		print('|_', end='')
		max_top -= 1

	for top in range(max_top):
		print('|___', end='')

	if top < max_top and top + 0.5 < max_top:
		if is_even:
			print('|_', end='')
		else:
			print('|_', end='')

	if odd or (i % 1.0 > 0 and i % 1.0 < 1):
		if is_even:
			print('__|', end='')
		else:
			print('|_|', end='')
	else:
		print('|', end='')
	
	print()
