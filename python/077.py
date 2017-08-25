from helpers import get_prime_numbers_until

primes = get_prime_numbers_until(1000)
target_combinations = 5000


def get_combinations(target, cur_amount, min_choice):
    posibilities = 0
    for choice in primes:
        if choice < min_choice:
            continue
        new_amount = cur_amount + choice
        if new_amount == target:
            posibilities += 1
            break
        elif new_amount > target:
            break

        posibilities += get_combinations(target, new_amount, choice)
    return posibilities

num = 2
while True:
    combs = get_combinations(num, 0, 1)
    print(num, combs)
    if combs >= target_combinations:
        break
    num += 1
print(num)

# j = 1
# while True:
#     combinations = {
#         0: 1
#     }
#     for prime in primes:
#         for i in range(1, j + 2):
#             if i >= prime:
#                 combinations[j] = combinations.get(i, 0) + combinations[i - prime]
#     print(combinations)
#     if combinations[j] >= 5000:
#         break
#         j += 1
# print(i)