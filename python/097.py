# print(str(28433 * (2 ** 7830457) + 1)[-10:])

i = 28433
j = 1
while j <= 7830457:
    j += 1
    i *= 2
    i = i % 10000000000

i += 1

print(i)