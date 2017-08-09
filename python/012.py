from helpers import get_next_prime, is_prime, get_xth_prime_number

divisable_by = {}


def get_divisables(number):
    if number in divisable_by:
        return divisable_by[number]

    if is_prime(number):
        divisable_by[number] = [1, number]
        return [1, number]

    divisor = 2
    while True:
        if number % divisor == 0:
            break
        divisor = get_next_prime(divisor)

    divisors = get_divisables(number / divisor) + [number]
    to_add = []
    for divisor in divisors:
        to_add.append(number / divisor)
    divisors += to_add

    divisors = list(set(divisors))
    divisable_by[number] = divisors
    return divisors

num = 1
step = 2
while True:
    if num % 12 == 0 and len(get_divisables(num)) > 500:
        break
    num += step
    step += 1

print(num)