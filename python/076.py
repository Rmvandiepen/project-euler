numbers = list(range(1, 100))
target = 100


def second_try():
    combinations = {
        0: 1
    }
    for number in numbers:
        for i in range(1, target + 1):
            if i >= number:
                combinations[i] = combinations.get(i, 0) + combinations[i - number]
    return combinations[target]

print(second_try())
