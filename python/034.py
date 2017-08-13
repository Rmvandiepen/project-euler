from helpers import get_factorial

def calc_max_digits():
	digits = 2
	while True:
		if get_factorial(9) * digits < 10 ** digits:
			return digits
		digits += 1

def is_curious_number(number):
	return number == sum([get_factorial(int(digit)) for digit in str(number)])

max_number = 10 ** calc_max_digits()
curious_numbers = []
for i in range(3, max_number):
	if is_curious_number(i):
		curious_numbers.append(i)
print(sum(curious_numbers))