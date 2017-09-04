# import math
#
# from helpers import time_spend_start, time_spend_end, pt
#
# minimum = int(math.sqrt(10 ** 18))
# maximum = int(math.sqrt(10 ** 18 * 2))
# print(len(str(maximum - minimum)))
# print(minimum)
# for i in range(1071926120, maximum, 10):
#     if i == 1081926120:
#         break
#     print(i, maximum)
#     time_spend_start('string')
#     string = str(i ** 2)
#     time_spend_end('string')
#     time_spend_start('if')
#     if string[0] == '1' \
#             and string[2] == '2' \
#             and string[4] == '3' \
#             and string[6] == '4' \
#             and string[8] == '5' \
#             and string[10] == '6' \
#             and string[12] == '7' \
#             and string[14] == '8' \
#             and string[16] == '9' \
#             and string[18] == '0':
#         break
#     time_spend_end('if')
# # pt()
# #
# # print(string)
# import math

a = {
    1: '0',
    3: '9',
    5: '8',
    7: '7',
    9: '6',
    11: '5',
    13: '4',
    15: '3',
    17: '2',
    19: '1'
}
import math

numbers = [0]
tried = []
position = 0
i = 0

# minimum = int(int(math.sqrt(1020304050607080900)) / 100)
# maximum = int(int(math.sqrt(1929394959697989990)) / 100)
# # print(minimum, maximum)
# for i in range(minimum, maximum):
#     for x in [30, 70]:
#         y = i * 100 + x
#         power = y ** 2
#         string = str(power)
#         if string[0] == '1' \
#                 and string[2] == '2' \
#                 and string[4] == '3' \
#                 and string[6] == '4' \
#                 and string[8] == '5' \
#                 and string[10] == '6' \
#                 and string[12] == '7' \
#                 and string[14] == '8' \
#                 and string[16] == '9' \
#                 and string[18] == '0':
#             print(y)
#             break
#     else:
#         continue
#     break
# print(i, x, string)
while i < 6:
    new_numbers = []
    for num in numbers:
        if num in tried:
            continue
        length = len(str(num))
        for digit in range(0, 10):
            new_num = num + digit * 10 ** i
            # print(new_num)
            d = len(str(new_num))
            value = str(new_num ** 2)
            if len(value) > 19:
                continue
            valid = True
            for b, c in a.items():
                # print(d, b, c)
                if d >= b and value[b * -1] != c:
                    valid = False
            if valid:
                # print(new_num)
                new_numbers.append(new_num)
            # continue
        tried.append(num)
    numbers = new_numbers
    # print(numbers)
    i += 1
print(sorted(numbers))
