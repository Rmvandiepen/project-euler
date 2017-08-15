from helpers import get_divisables

total = 0
for x in range(2, 10000 + 1):
    divisables = list(get_divisables(x))
    divisables.remove(x)
    sum_of_divisables = sum(divisables)
    if x == sum_of_divisables:
        continue

    divisables = list(get_divisables(sum_of_divisables))
    divisables.remove(sum_of_divisables)
    sum_of_divisables = sum(divisables)

    if sum_of_divisables == x:
        total += x

print(total)
