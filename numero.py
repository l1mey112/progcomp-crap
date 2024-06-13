amount = int(input())

conv = {
	'M': 1000,
	'D': 500,
	'C': 100,
	'L': 50,
	'X': 10,
	'V': 5,
	'I': 1,
}

conv_subs = ['C', 'X', 'I']

def make_p(a: str, b: str):
	return a.ljust(7) + b

for _ in range(amount):
	largest = None
	line = input()

	idx = 0
	backwards = line[::-1]

	def main():
		if backwards == '':
			print(make_p('Bad1', line))
			return
		
		running_sum = 0
		largest = None
		for idx, ch in enumerate(backwards):
			if ch not in conv:
				print(make_p('Bad1', line))

			value = conv[ch]
			if not largest:
				largest = value

			if value < largest:
				if idx > 0 and conv[backwards[idx - 1]] > value:
					print(make_p('Bad2', line))
					return
				
				# subtract
				if ch not in conv_subs:
					print(make_p('Bad4', line))
					return

				running_sum -= value
			else:
				running_sum += value
				largest = value

		print(make_p(str(running_sum), line))

	main()

	