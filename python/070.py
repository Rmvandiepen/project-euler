import itertools

from helpers import get_prime_divisables, is_prime, get_prime_numbers_until, st, pt, time_spend_start, time_spend_end, \
    get_prime_factors, is_permutation

highest_n = (0, 0)
st()
lowest = (2, 2)

for n in range(2, 10 ** 7):
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        continue

    time_spend_start('prime_factor')
    prime_factors = set(get_prime_factors(n))
    time_spend_end('prime_factor')

    time_spend_start('calc')
    a = sum([n / x - 1 for x in prime_factors])
    b = sum([n / (x * y) - 1 for x, y in itertools.combinations(prime_factors, 2)])
    relative_primes = int(n - 1 - (a - b))
    time_spend_end('calc')
    time_spend_start('is_perm')
    if is_permutation(n, relative_primes):
        score = n / relative_primes
        print('is_perm', n, relative_primes, score)
        if score < lowest[0]:
            lowest = (score, n)
    time_spend_end('is_perm')
print(lowest)

pt()
