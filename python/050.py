from helpers import get_prime_numbers_until, st, pt


def first_try():
    primes = get_prime_numbers_until(1000000)
    max_consecutive_prime = 0
    max_consecutive = 2
    for prime in reversed(primes):
        starting_primes = [p for p in primes if p < prime / max_consecutive]
        for index, sp in enumerate(starting_primes):
            prime_sum = 0
            index_offset = 0
            while prime_sum < prime:
                prime_sum += primes[index + index_offset]
                index_offset += 1
            if prime_sum == prime and index_offset > max_consecutive:
                max_consecutive = index_offset
                max_consecutive_prime = prime
                print(prime, index_offset, len(starting_primes))
                break
            elif prime_sum > prime and index_offset < max_consecutive:
                break
    return max_consecutive, max_consecutive_prime


def second_try():
    max_consecutive = 0
    primes = get_prime_numbers_until(1000000)
    last_prime = primes[len(primes) - 1]
    for index, prime in enumerate(primes):
        if prime * max_consecutive > last_prime:
            break

        prime_sum = 0
        index_offset = 0
        while prime_sum < last_prime:
            prime_sum += primes[index + index_offset]
            if index_offset > max_consecutive and prime_sum in primes:
                max_consecutive = index_offset
                max_consecutive_prime = prime_sum
            index_offset += 1
    return max_consecutive, max_consecutive_prime

print(second_try()[1])

