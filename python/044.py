pentagonal_numbers = {}
highest_pentagonal = 0
pentagonal_index = 0


def get_next_pentagonal_number():
    global highest_pentagonal, pentagonal_index
    pentagonal_index += 1
    highest_pentagonal = int(pentagonal_index * (3 * pentagonal_index - 1) / 2)
    pentagonal_numbers[pentagonal_index] = highest_pentagonal


def is_pentagonal(number):
    while highest_pentagonal < number:
        get_next_pentagonal_number()
    return number in pentagonal_numbers.values()


def get_pentagonal_number(n):
    while n not in pentagonal_numbers:
        get_next_pentagonal_number()
    return pentagonal_numbers[n]


# j = 2100
# while True:
# # for j in range(1, 100):
#     print(j)
#     j_pentagonal = get_pentagonal_number(j)
#     # print(j, j * 100, is_pentagonal(j))
#     # print(pentagonal_numbers)
#     for k in range(j -1, 0, -1):
#         k_pentagonal = get_pentagonal_number(k)
#         sum_pentagonal = j_pentagonal + k_pentagonal
#         difference_pentagonal = abs(k_pentagonal - j_pentagonal)
#         if j == 2167 and k > 1000:
#             print(j_pentagonal, k_pentagonal, sum_pentagonal, difference_pentagonal)
#         # if is_pentagonal(difference_pentagonal):
#         #     print(j, k, difference_pentagonal)
#             # print(pentagonal_numbers)
#         if is_pentagonal(sum_pentagonal) and is_pentagonal(difference_pentagonal):
#             print(j, k)
#             break
#     else:
#         j += 1
#         continue
#     break


pentset = set()
i = 1
check = False

while not check:
    ti = i * (3 * i - 1) / 2
    for j in pentset:
        if ti - j in pentset and ti - 2 * j in pentset:
            print(ti - 2 * j)
            check = True
            break
    pentset.add(ti)
    i += 1
