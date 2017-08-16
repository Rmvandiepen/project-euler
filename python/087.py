from helpers import get_prime_numbers_until

target = 50 * 10 ** 6
primes_1 = get_prime_numbers_until(int(target ** (1/2)) + 1)
primes_2 = get_prime_numbers_until(int(target ** (1/3)) + 1)
primes_3 = get_prime_numbers_until(int(target ** (1/4)) + 1)
numbers = set()
itters = 0
for prime_1 in primes_1:
    prime_1_square = prime_1 ** 2
    for prime_2 in primes_2:
        prime_2_cube = prime_2 ** 3
        if prime_1_square + prime_2_cube > target:
            primes_2 = [prime for prime in primes_2 if prime < prime_2]

        for prime_3 in primes_3:
            prime_3_fourth = prime_3 ** 4

            if prime_1_square + prime_3_fourth > target:
                primes_3 = [prime for prime in primes_3 if prime < prime_3]
            num = prime_1_square + prime_2_cube + prime_3_fourth
            if num < target:
                numbers.add(num)
            itters += 1

print(itters)
print(len(numbers))
