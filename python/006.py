def square_of_sum(numbers):
    return sum([number ** 2 for number in numbers])


def sum_of_square(numbers):
    return sum([number for number in numbers]) ** 2


numbers = range(1, 20 + 1)
sum_of_square = sum_of_square(numbers)
square_of_sum = square_of_sum(numbers)
difference = abs(sum_of_square - square_of_sum)

print(sum_of_square)
print(square_of_sum)
print(difference)