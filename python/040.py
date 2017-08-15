numbers = [1, 10, 100, 1000, 10000, 100000, 1000000]
highest_number = max(numbers)
i = 1
string = ''
while True:
    string += str(i)
    i += 1
    if len(string) > highest_number:
        break

result = 1
for number in numbers:
    result *= int(string[number - 1])
print(result)