import math

a = 1
b = 2
while True:
    c = math.sqrt(a ** 2 + b ** 2)
    if a + b + c == 1000:
        result = a * b * c
        break
    elif a + b + c > 1000:
        a += 1
        b = a + 1
    else:
        b += 1

print(result)