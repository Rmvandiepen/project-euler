
next_primes = {
    2: 3
}


def get_prime_numbers_until(highest_number):
    prime_numbers = [True for _ in range(int(highest_number))]
    for x in range(2, int(highest_number ** 0.5)):
        if not prime_numbers[x]:
            continue
        y = x
        while x * y < highest_number:
            prime_numbers[x * y] = False
            y += 1
    return [i for i, value in enumerate(prime_numbers) if value and i > 1]


def is_prime(number):
    if number % 2 == 0:
        return False
    for num in range(3, int(number ** 0.5) + 1, 2):
        if number % num == 0:
            return False
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
        prime_number += 2

    next_primes[start_prime] = prime_number
    return prime_number


def is_palindrome(num):
    return True if str(num) == str(num)[::-1] else False
