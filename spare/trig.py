import math
from collections import deque

def program_a(array: list):
	if len(array) == 1:
		return array[0]

	l = array[0] + array[-1]

	for i in range(len(array) - 1):
		left = array[i]
		right = array[i + 1]

		# trig
		l += math.sqrt((left + right) ** 2 - abs(left - right) ** 2)

	return l

def program_b(array: list):
	array.sort(reverse=True)
	ndeqeue = deque(array)
	items = deque([ndeqeue.popleft()])

	side = True # smallest side

	while len(ndeqeue) > 1:
		if side:
			items.append(ndeqeue.pop())
			items.appendleft(ndeqeue.pop())
		else:
			items.append(ndeqeue.popleft())
			items.appendleft(ndeqeue.popleft())

		side = not side

	if len(ndeqeue) > 0:
		last = ndeqeue.pop()
		left_diff = abs(items[0] - last)
		right_diff = abs(items[-1] - last)

		if left_diff > right_diff:
			items.appendleft(last)
		else:
			items.append(last)		

	return list(items)

out = program_a([3, 7, 4, 9.5, 12])
print(round(out, 2))

out = program_b([3, 7, 4, 9.5, 12])
print(out)
