from helpers import product

def first_solution():
	string = ''
	posibilities_left = 10 ** 6 - 1
	numbers_left = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	while True:
		number = 0
		to_substract = 0
		for x in range(1, len(numbers_left) + 1):
			posibilities_with_nums = product(list(range(1, x + 1)))
			if posibilities_with_nums > posibilities_left:
				to_substract = product(list(range(1, x)))
				break
			elif posibilities_with_nums == posibilities_left:
				to_substract = product(list(range(1, x + 1)))
				break
		fits = int(posibilities_left / to_substract)
		number = numbers_left.pop(fits)
		string += str(number)
		posibilities_left -= int(posibilities_left / to_substract) * to_substract
		if posibilities_left == 0:
			break
	string += ''.join([str(num) for num in numbers_left])
	return string
print(first_solution())

def second_solution():
	max_num = 9
	cur_string = ''
	def get_nums(nums):
		pos = []
		for x in range(0, max_num + 1):
			if x in nums:
				continue
			if len(nums) == max_num:
				return [''.join([str(num) for num in nums + [x]])]
			else:
				pos += get_nums(nums + [x])
		return pos

	posibiities = get_nums([])
	return posibiities[1000000 - 1]

# print(second_solution())
