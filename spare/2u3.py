def P():
	k = 2
	p_k = 1.0
	while True:
		p_k *= (k ** 3 - 1) / (k ** 3 + 1)

		if p_k < 0.6666667000:
			return k - 1, round(p_k / ((k ** 3 - 1) / (k ** 3 + 1)), 16)

		k += 1

print(P())
