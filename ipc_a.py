import math

amount = int(input())

for _ in range(amount):
	line = input().split(' ')
	n = int(line[0])
	d = int(line[1])

	print(math.ceil((n - 1) / (d + 1)))

""" 
# 4 compounds
# 1 day

# day 1:
# site 1: 2 compounds
# site 2: 2 compounds

# day 2:
# site 1: 1 compound
# site 2: 1 compound """


# 4 compounds
# 1 day

# 


# _x
# x_
# xx

# 3^4 = 81 - 3 = 73

# xx
# xx
# xx
# xx