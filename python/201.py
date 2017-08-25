numbers = [num ** 2 for num in range(1, 101)]
cur_numbers = numbers[:50]

print(numbers[:50])
print(numbers[50:])
print(sum(numbers[:50]))
print(sum(numbers[50:]))
print(sum(numbers[50:]) - sum(numbers[:50]))