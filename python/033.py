from helpers import get_smallest_fraction


curious_fractions = []
for numerator in range(11, 100):
	if numerator % 10 == 0:
		continue
	for denominator in range(numerator, 100):
		if numerator == denominator or denominator % 10 == 0:
			continue
		first_digit_numerator = str(numerator)[0]
		second_digit_numerator = str(numerator)[1]
		first_digit_denominator = str(denominator)[0]
		second_digit_denominator = str(denominator)[1]
		str_denominator = str(denominator)
		new_numerator = 0
		new_denominator = 0
		if first_digit_numerator == second_digit_denominator and second_digit_numerator != first_digit_denominator:
			new_numerator = int(second_digit_numerator)
			new_denominator = int(first_digit_denominator)
		elif second_digit_numerator == first_digit_denominator and first_digit_numerator != second_digit_denominator:
			new_numerator = int(first_digit_numerator)
			new_denominator = int(second_digit_denominator)

		if new_numerator and numerator / denominator == new_numerator / new_denominator:
			curious_fractions.append((numerator, denominator))

total_numerator = 1
total_denominator = 1

for curious_fraction in curious_fractions:
	numerator, denominator = get_smallest_fraction(curious_fraction[0], curious_fraction[1])
	total_numerator *= numerator
	total_denominator *= denominator

numerator, denominator = get_smallest_fraction(total_numerator, total_denominator)
print(denominator)
