
i = 1
fraction = (3, 2)
result = 0
while i < 1000:
    fraction = (fraction[0] + 2 * fraction[1], fraction[0] + fraction[1])
    if len(str(fraction[0])) > len(str(fraction[1])):
        result += 1
    i += 1
print(result)
