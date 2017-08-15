coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200


def first_try():
    def try_posibility(cur_amount, min_choice):
        posibilities = 0
        for choice in coins:
            if choice < min_choice:
                continue
            new_amount = cur_amount + choice
            if new_amount == target:
                posibilities += 1
                break
            elif new_amount > target:
                break

            posibilities += try_posibility(new_amount, choice)
        return posibilities

    return try_posibility(0, 1)


def second_try():
    combinations = {
        0: 1
    }
    for coin in coins:
        for i in range(1, target + 1):
            if i >= coin:
                combinations[i] = combinations.get(i, 0) + combinations[i - coin]
    return combinations[target]

print(second_try())
# print(first_try())
