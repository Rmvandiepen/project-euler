num = 20
step = num * (num - 1)
i = step
result = 0
while True:
    correct = True
    for x in range(10, num + 1):
        if i % x != 0:
            correct = False
            break
    if correct:
        result = i
        break
    i += step
print(result)
