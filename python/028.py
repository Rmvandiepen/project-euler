size = 1001
result = {}

min_x = 1
min_y = 2
max_x = max_y = size

cur_x = max_x
cur_y = 1

dir_x = -1
dir_y = 0

num = size ** 2

def print_result(result):
	print('----')
	for y in range(1, size + 1):
		line = ''
		for x in range(1, size + 1):
			line += "%02d, " % result.get('{x},{y}'.format(x=x, y=y), 0)
		print(line)


while num > 0:
	result['{x},{y}'.format(x=cur_x, y=cur_y)] = num
	# print(dir_x, dir_y, cur_x, cur_y, min_x, min_y, max_x, max_y)
	if dir_x == -1 and cur_x == min_x:
		min_x += 1
		dir_x = 0
		dir_y = 1
	elif dir_x == 1 and cur_x == max_x:
		max_x -= 1
		dir_x = 0
		dir_y = -1
	elif dir_y == -1 and cur_y == min_y:
		min_y += 1
		dir_x = -1
		dir_y = 0
	elif dir_y == 1 and cur_y == max_y:
		max_y -= 1
		dir_x = 1
		dir_y = 0

	cur_x += dir_x
	cur_y += dir_y
	num -= 1

# print_result(result)

total = 0
for i in range(1, size + 1):
	total += result['{x},{y}'.format(x=i, y=i)]
	total += result['{x},{y}'.format(x=i, y=size + 1 - i)]

total -= 1
print(total)

# print(result)



