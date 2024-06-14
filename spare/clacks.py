def line(string):
	digits = []
	
	acc = 0
	place = 0
	for k in range(0, len(string), 2):
		v = string[k:k+2]

		if v == 'X.':
			digit = 0
		elif v == '.X':
			digit = 1
		elif v == '..':
			digit = 2
		else:
			return '#'

		digits.append(digit)

		acc += digit * (3 ** place)
		place += 1

	has = True
	for i in digits[1:]:
		if i != digits[0]:
			has = False
	if has:
		if digits[0] == 2:
			return 'LOCKOUT'
		else:
			return '#'

	lut = '_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm_nopqrstuvwxyz0123456789 !"$%&\'()*,-.:?@'

	return lut[acc]

amount = int(input())

acc = ''
for _ in range(amount):
	l = line(input())
	if l == 'LOCKOUT':
		break
	acc += l

print(acc)

if l == 'LOCKOUT':
	print(l)