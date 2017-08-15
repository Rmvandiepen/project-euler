from helpers import is_prime

digits = list(range(1, 11))


def try_prime(number):
    truncatable_primes = []
    if number > 9 and is_truncatable_prime(number):
        truncatable_primes.append(number)

    new_value = number * 10
    for digit in digits:
        new_prime = new_value + digit
        if is_prime(new_prime):
            truncatable_primes += try_prime(new_value + digit)
    return truncatable_primes


def is_truncatable_prime(number):
    if not is_prime(number):
        return False
    number = str(number)
    for x in range(1, len(number)):
        if not is_prime(int(number[:-x])) or not is_prime(int(number[x:])):
            return False
    return True

truncatable_primes = try_prime(0)
print(sum(truncatable_primes))
