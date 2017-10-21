numbers = []
power = 5


def get_sum_of_number(number):
    return sum([int(digit) ** power for digit in str(number)])


def calc_max_digits():
    digits = 2
    max_per_digit = 9 ** power
    while True:
        if digits * max_per_digit < 10 ** digits:
            return digits
        digits += 1


max_number = 10 ** calc_max_digits()
i = 2
while True:
    if i == get_sum_of_number(i):
        numbers.append(i)
    i += 1
    if i >= max_number:
        break

print(numbers)
print(sum(numbers))
