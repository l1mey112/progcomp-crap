import math

def encode(g: int):
	k = 0
	r = 0

	for s in str(g).rjust(4, "0"):
		c = int(s)

		d = (3 * c + 7) % 10
		r = r + 2 ** (3 * d + 2) + k * 8 ** d
		k += 1

	return r

def match(gcode: int, scode: int):
	b = ""
	c = ""

	for k in range(0, 10):
		p = math.floor(gcode / 8 ** k) % 8
		q = math.floor(scode / 8 ** k) % 8

		r = p - q

		s = 2 * r + 3 * q

		if s > 11 and s > 2 * r:
			if s == 3 * p:
				b += "B"
			else:
				c += "C"

	return b + c

def main(secret_enc: int):
	def is_not_duplicate(d: int):
		ds = str(d)

		while len(ds) < 4:
			ds = "0" + ds

		set_digits = set()

		for s in ds:
			if s in set_digits:
				return False

			set_digits.add(s)

		return True

	numbers = list(filter(is_not_duplicate, range(0, 10000)))

	print(f'Initial candidate list size = {len(numbers)}.')
	guesses = 1

	while True:
		l = len(numbers)
		if l % 2 == 0:
			idx = math.ceil(l / 2)
		else:
			idx = l // 2

		midpoint = numbers[idx]
		score = match(encode(midpoint), secret_enc)

		if score == "BBBB":
			print('Solution:', midpoint)
			return

		numbers.remove(midpoint)

		for k in numbers.copy():
			kscore = match(encode(k), encode(midpoint))
			if kscore == score:
				pass
			else:
				numbers.remove(k)

		print(f'Guess {guesses} {midpoint} gives {score.ljust(4)} Candidates remaining:', len(numbers))
		guesses += 1


main(12748856)
