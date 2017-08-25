max_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        digital_sum = sum([int(char) for char in str(a ** b)])
        max_sum = max(max_sum, digital_sum)
print(max_sum)