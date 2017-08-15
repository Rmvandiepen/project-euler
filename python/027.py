from helpers import is_prime, get_prime_numbers_until

highest_combo = (0, 0, 0)
primes = get_prime_numbers_until(1001)

for a in range(-999, 1000):
    for b in primes:
        n = 0
        while True:
            number = n ** 2 + a * n + b
            if number < 2 or not is_prime(number):
                n -= 1
                if n > highest_combo[2]:
                    print('new high', a, b, n)
                    highest_combo = (a, b, n)
                break
            n += 1

print(highest_combo[0] * highest_combo[1])


