import itertools

from helpers import time_spend_start, time_spend_end, pt, st, get_prime_factors, precalc_primes_until

st()

target = 10 ** 6
count = 0
phi = list(range(0, target + 1))
for d in range(2, target + 1):
    # if d % 10 ** 5 == 0:
    #     print(d)
    if phi[d] == d:
        for j in range(d, target + 1, d):
            phi[j] = phi[j] / d * (d - 1)
    # print(d, phi[d])
    count += phi[d]

print(count)

pt()
