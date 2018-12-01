from collections import defaultdict
from decimal import Decimal

from helpers import st, pt


def try_one():
    peters = (4, 6)
    colins = (6, 4)

    peter_win = 0
    total = peters[0] ** peters[1] * colins[0] ** colins[1]
    percent = 0
    percent_increment = 10
    for i in range(0, total):
        if i >= int((total / 100)) * (percent + percent_increment):
            percent += percent_increment
            print(f'At {percent}%')
        tmp_i = i
        peters_num = 0
        for _ in range(0, peters[1]):
            num = tmp_i % peters[0]
            tmp_i = int(tmp_i / peters[0])
            peters_num += num + 1

        colins_num = 0
        for _ in range(0, colins[1]):
            num = tmp_i % colins[0]
            tmp_i = int(tmp_i / colins[0])
            colins_num += num + 1

        if peters_num > colins_num:
            peter_win += 1
    print(peter_win, total, peter_win/total)
    return peter_win/total


def try_two():
    peters = (4, 9)
    colins = (6, 6)

    def calc_results(dice_size, dice_num):
        results = defaultdict(int)
        total = dice_size ** dice_num
        for i in range(0, total):
            result = 0
            for _ in range(0, dice_num):
                num = i % dice_size
                i = int(i / dice_size)
                result += num + 1
            results[result] += 1
        return {result: times/total for result, times in results.items()}

    peters_results = calc_results(peters[0], peters[1])
    colins_results = calc_results(colins[0], colins[1])

    win = draw = loss = Decimal(0)

    for peter_result, peter_chance in peters_results.items():
        for colin_result, colin_chance in colins_results.items():
            chance = Decimal(peter_chance * colin_chance)
            if peter_result > colin_result:
                win += chance
            elif peter_result == colin_result:
                draw += chance
            elif peter_result < colin_result:
                loss += chance

    return round(win, 7)

# try_one()
st()
print(try_two())
pt()
