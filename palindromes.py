import regex

amount = int(input())

for _ in range(amount):
	line = input()
	nline = regex.sub(r'[!@#$%^&\*\(\)\?:;,\.\[\]\-_\+~\` \'\"]', '', line)
	nline = nline.lower()

	pal = True
	for i in range(len(nline) // 2):
		if nline[i] != nline[-i - 1]:
			pal = False

	if pal:
		print(f'Yes "{line}"')
	else:
		print(f' No "{line}"')
