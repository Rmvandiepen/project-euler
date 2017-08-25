power = 1

result = 0
while True:
    for i in range(1, 10):
        if len(str(i ** power)) == power:
            print(i, power, i ** power)
            result += 1
        elif i == 9:
            break
    else:
        power += 1
        continue
    break
print(result)