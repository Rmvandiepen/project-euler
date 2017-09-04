import itertools

from helpers import time_spend_start, time_spend_end, pt, st, get_prime_factors, precalc_primes_until

next_primes = dict()
primes = set()


# def get_prime_factors(number):
#     global primes
#     if number in primes:
#         return [number]
#
#     pfs = []
#     while number != 1:
#         prime = 2
#         while number % prime != 0:
#             prime = next_primes[prime]
#         pfs.append(prime)
#         number /= prime
#
#     return pfs
#
#
# def pre_calc_primes(highest_number):
#     global next_primes, primes
#     prime_numbers = [True] * highest_number
#     for x in range(2, int(highest_number ** 0.5) + 1):
#         if not prime_numbers[x]:
#             continue
#         y = x
#         while x * y < highest_number:
#             prime_numbers[x * y] = False
#             y += 1
#     primes = [i for i, value in enumerate(prime_numbers) if value and i > 1]
#     for index, prime in enumerate(primes[:-1]):
#         next_primes[prime] = primes[index + 1]
#     primes = set(primes)

st()

target = 10 ** 6
precalc_primes_until(target)
count = 0
for d in range(2, target + 1):
    if d % 10 ** 5 == 0:
        print(d)
    prime_factors = set(get_prime_factors(d))
    # print(d, prime_factors)
    a = sum([d / x - 1 for x in prime_factors])
    b = sum([d / (x * y) - 1 for x, y in itertools.combinations(prime_factors, 2)])
    count += int(d - 1 - (a - b))

print(count)

pt()