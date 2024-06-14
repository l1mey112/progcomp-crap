actors = int(input())

stages = [
	["-"] * actors,
]

def swap(x: str):
	if x == "-":
		return "X"
	else:
		return "-"

print(f'{" ".join(["-"] * actors)}')

while True:
	found = False
	for idx in range(actors):
		nstage = stages[-1].copy()
		nstage[idx] = swap(nstage[idx])

		if nstage in stages:
			continue
		
		stages.append(nstage)
		found = True

		status = 'Leave' if nstage[idx] == '-' else 'Enter'

		status_stages = []
		for stage_idx, stat in enumerate(nstage):
			if stat == 'X':
				status_stages.append(str(stage_idx + 1))

		print(f'{status} {idx + 1} {" ".join(status_stages)} {" ".join(nstage)}')
		break

	if not found:
		print(f'Leave {actors} {" ".join(["-"] * actors)}')
		break