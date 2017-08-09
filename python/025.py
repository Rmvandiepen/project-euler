first = 1
second = 1
i = 3
while True:
    new_first = second
    second = first + second
    first = new_first
    if len(str(second)) >= 1000:
        break
    i += 1
print(i)