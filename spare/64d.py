doors = [False] * 64

for i in range(64):
	for idx in range(64):
		if (idx + 1) % (i + 1) == 0:
			doors[idx] = not doors[idx]

for idx in range(64):
	if doors[idx]:
		print(idx + 1)