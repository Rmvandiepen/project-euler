import math

minimum = int(int(math.sqrt(1020304050607080900)) / 100)
maximum = int(int(math.sqrt(1929394959697989990)) / 100)
result = 0
for i in range(minimum, maximum):
    for x in [30, 70]:
        y = i * 100 + x
        power = y ** 2
        string = str(power)
        if string[0] == '1' \
                and string[2] == '2' \
                and string[4] == '3' \
                and string[6] == '4' \
                and string[8] == '5' \
                and string[10] == '6' \
                and string[12] == '7' \
                and string[14] == '8' \
                and string[16] == '9' \
                and string[18] == '0':
            result = y
            break
    else:
        continue
    break
print(result)
