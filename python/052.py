from collections import Counter

x = 1
while True:
    digits = Counter(list(str(x * 2)))
    for i in range(3, 7):
        if Counter(list(str(x * i))) != digits:
            break
    else:
        break
    x += 1
print(x)
