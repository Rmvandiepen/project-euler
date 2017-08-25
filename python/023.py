from helpers import get_divisables

abundent_numbers = []
max_number = 28123
for x in range(1, max_number + 1):
    divisors = get_divisables(x)
    divisors.remove(x)
    sum_of_divisors = sum(divisors)
    if sum_of_divisors > x:
        abundent_numbers.append(x)

numbers = {num: False for num in range(1, max_number + 1)}
for x in abundent_numbers:
    for y in abundent_numbers:
        numbers[sum([x, y])] = True

not_sumable = [key for key, value in numbers.items() if not value]
print(sum(not_sumable))
