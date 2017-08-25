import time
from collections import Counter, defaultdict

start_time = 0

# time_spend_start_time = 0
# time_spend = 0
time_spend_start_times = {}
time_spend = defaultdict(int)

next_primes = {
    2: 3
}
divisable_by = {
    1: [1]
}
calculated_primes = {
    1: False,
    2: True
}
pandigital_digits = {}

calculated_primes_until_list = []
calculated_primes_until = 0


def get_prime_numbers_until(highest_number):
    global calculated_primes_until, calculated_primes_until_list
    if highest_number <= calculated_primes_until:
        return [prime for prime in calculated_primes_until_list if prime < highest_number]

    prime_numbers = [True] * highest_number
    for x in range(2, int(highest_number ** 0.5) + 1):
        if not prime_numbers[x]:
            continue
        y = x
        while x * y < highest_number:
            prime_numbers[x * y] = False
            y += 1
    primes = [i for i, value in enumerate(prime_numbers) if value and i > 1]
    calculated_primes_until_list = list(primes)
    calculated_primes_until = highest_number
    return primes


def is_prime(number):
    if number in calculated_primes:
        return calculated_primes[number]

    if number % 2 == 0:
        calculated_primes[number] = False
        return False

    for num in range(3, int(number ** 0.5) + 1, 2):
        if number % num == 0:
            calculated_primes[number] = False
            return False

    calculated_primes[number] = True
    return True


def get_xth_prime_number(x):
    iteration = 1000
    while True:
        prime_numbers = get_prime_numbers_until(iteration)
        if len(prime_numbers) > x:
            return prime_numbers[x-1]
        iteration *= 1000


def get_next_prime(prime_number):
    if prime_number in next_primes:
        return next_primes[prime_number]

    start_prime = prime_number
    prime_number += 2
    while not is_prime(prime_number):
        calculated_primes[prime_number] = False
        prime_number += 2

    calculated_primes[prime_number] = True
    next_primes[start_prime] = prime_number
    return prime_number


def is_palindrome(num):
    return True if str(num) == str(num)[::-1] else False


def is_pandigital(value, start=1):
    digits = list(str(value))
    digits_length = len(digits)
    if digits_length != len(set(digits)):
        return False
    if (start, digits_length) not in pandigital_digits:
        pandigital_digits[start, digits_length] = Counter([str(digit) for digit in range(start, digits_length + start)])
    return Counter(digits) == pandigital_digits[start, digits_length]


def get_divisables(number):
    if number in divisable_by:
        return list(divisable_by[number])

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
    return list(divisors)


def get_prime_divisables(number):
    time_spend_start('divisables')
    divisables = get_divisables(number)
    time_spend_end('divisables')
    time_spend_start('primes')
    res = [prime for prime in divisables if is_prime(prime)]
    time_spend_end('primes')
    return res


def get_prime_factors(number):
    if is_prime(number):
        return [number]

    prime_factors = []
    divisables = get_divisables(number)
    for divisor in divisables:
        if is_prime(divisor):
            prime_factors.append(divisor)
            number /= divisor

    if number > 1:
        prime_factors += get_prime_factors(number)
    return sorted(prime_factors)


def product(int_list):
    result = 1
    for x in int_list:
        result *= x
    return result


def get_factorial(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


def calculate_combinatorics(n, r):
    return int(get_factorial(n) / (get_factorial(r) * get_factorial(n - r)))


def get_smallest_fraction(numerator, denominator):
    divisor = get_biggest_common_divisor(numerator, denominator)
    return int(numerator / divisor), int(denominator / divisor)


def get_biggest_common_divisor(num1, num2):
    divisables_num1 = get_divisables(num1)
    divisables_num2 = get_divisables(num2)
    common_divisables = set(divisables_num1).intersection(divisables_num2)
    return max(common_divisables)


def get_base_x_value(number, base):
    i = 1
    while True:
        if number < base ** i:
            power = i - 1
            break
        i += 1
    value = ''
    while power >= 0:
        base_power = base ** power
        if number >= base_power:
            fits = int(number / base_power)
            value += str(fits)
            number -= fits * base_power
        else:
            value += '0'
        power -= 1
    return value


def get_binary_value(number):
    return get_base_x_value(number, 2)


def st():
    global start_time
    start_time = int(time.time() * 1000)


def time_spend_start(tag):
    global time_spend_start_times
    time_spend_start_times[tag] = int(time.time() * 1000)


def time_spend_end(tag):
    global time_spend
    time_spend[tag] += int(time.time() * 1000) - time_spend_start_times[tag]


def pt():
    print('{time} ms'.format(time=int(time.time() * 1000) - start_time))
    if time_spend:
        print(dict(time_spend))
