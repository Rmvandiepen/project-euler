from helpers import st, pt, time_spend_start, time_spend_end

st()
# solutions_known = {}


def calc(x):
    str_x = str(x)
    reversed_x_str = str_x[::-1]
    # if reversed_x_str in solutions_known:
    #     return solutions_known[reversed_x_str], 0

    if reversed_x_str[0] == '0':
        return False, 0

    reversed_x = int(reversed_x_str)

    total = x + reversed_x

    str_total = str(total)
    str_length = len(str_total)

    success = True
    to_skip = 0
    for i, char in enumerate(str_total):
        i += 1
        middle = int((str_length + 1) / 2)

        if char in ('0', '2', '4', '6', '8'):
            success = False

            if len(str_x) != len(str_total):
                continue

            if 1 < i <= middle:
                power_num = 10 ** (i - 1)
                original_subtract = int(str_x[-i + 1:])
                reversed_subtract = int(reversed_x_str[-i + 1:])
                new_to_skip = power_num - original_subtract - reversed_subtract

                to_skip = max(to_skip, new_to_skip)

        if not success and i > middle:
            break

    if x == 10000000:
        print(x, to_skip)

    return success, to_skip


start = 0
end = 10 ** 9

num_skipped = 0
x = start

power = 1
target = 20
count_to_target = 0

count = 0
while x <= end:
    if x == target:
        print(f'At {x} counted {count_to_target}. power {power}')

        if power % 2 == 0 and x == int(2.1 * 10 ** power):
            print(f'At {x} adding {100 * count_to_target}')
            count += 100 * count_to_target
            x = 10 ** (power + 1)
            target = int(x * 1.1)
        elif power % 2 == 0 and x == 3 * 10 ** power:
            print(f'At {x} adding {20 * count_to_target}')
            count += 20 * count_to_target
            x = 10 ** (power + 1)
            target = int(x * 1.1)
        elif power % 2 == 1 and x == int(1.1 * 10 ** power):
            print(f'At {x} adding {30 * count_to_target}')
            count += 30 * count_to_target
            x = 10 ** (power + 1) * 2
            target = int(10 ** (power + 1) * 2.1)
        elif power % 2 == 1 and x == int(2 * 10 ** power):
            print(f'At {x} adding {5 * count_to_target}')
            count += 5 * count_to_target
            x = 10 ** (power + 1) * 2
            target = int(10 ** (power + 1) * 2.1)

        power += 1
        count_to_target = 0

    solution, skip = calc(x)
    if solution:
        count_to_target += 1

    num_skipped += skip
    x += 1 + skip
print('skipped', num_skipped)

print('result', count)
pt()
