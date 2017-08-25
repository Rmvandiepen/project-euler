from helpers import get_prime_divisables, is_prime, get_prime_numbers_until, st, pt, time_spend_start, time_spend_end

highest_n = (0, 0)
st()
min_prime_length = 0

for n in range(2, 1000000, 2):
    if n % 3 != 0 or n % 5 != 0:
        continue
    prime_divisables = get_prime_divisables(n)
    if len(prime_divisables) <= min_prime_length:
        continue
    min_prime_length = len(prime_divisables)
    time_spend_start('calc')
    relatively_primes_len = 0
    for i in range(1, n):
        for prime in prime_divisables:
            if i % prime == 0:
                break
        else:
            relatively_primes_len += 1

    time_spend_end('calc')
    score = n / relatively_primes_len
    if score > highest_n[1]:
        highest_n = (n, score)

print(highest_n)

pt()