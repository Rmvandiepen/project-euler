from helpers import get_prime_numbers_until

primes = get_prime_numbers_until(10 ** 8)
digits = {
    i: set([str(digit) for digit in range(1, i + 1)]) for i in range(1, 10)
}
prime = primes[-10:][1]
for prime in reversed(primes):
    prime_len = len(str(prime))
    if set(list(str(prime))) == digits[prime_len]:
        break

print(prime)