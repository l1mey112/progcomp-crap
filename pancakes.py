import math
from typing import List, Tuple

line = input()

pancakes: List[Tuple[float, bool]] = []

for part in line.split(' '):
	burnt = False
	if part.endswith('*'):
		burnt = True
		part = part[:-1]

	part = float(part)

	pancakes.append((part, burnt))

def perform_spatula(a: int):
	top = a + math.ceil((len(pancakes) - a) / 2)

	for i in range(a, top):
		topc = top - i - 1
		tmp = pancakes[i]
		pancakes[i] = (pancakes[topc][0], not pancakes[topc][1])
		pancakes[topc] = (tmp[0], not tmp[1])

	com = [f'{a}:']

	for k in pancakes:
		v, burnt = k
		com.append(str(v) + ('*' if burnt else ''))

	print(" ".join(com))

def is_order(bottom, top):
	if bottom[0] >= top[0]:
		return True

print(pancakes)

sorted_stuff = pancakes.copy()
sorted_stuff.sort(key=lambda x: x[0], reverse=True)

init_partition = 0
for i in range(len(pancakes)):
	if sorted_stuff[i][0] != pancakes[i][0]:	
		break
	init_partition += 1

for i in range(init_partition):
	if pancakes[i][1]:
		perform_spatula(i)
		perform_spatula(len(pancakes) - 1)
		perform_spatula(i)
