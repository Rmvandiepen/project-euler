product = 1
for x in range(1, 100 + 1):
    product *= x

sum_of_total = 0
for digit in str(product):
    sum_of_total += int(digit)

print(sum_of_total)