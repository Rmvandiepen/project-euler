from helpers import is_prime

size = 1
value = 1

total = 1
primes = 0
while True:
    size += 2

    top_right_value = value + size - 1
    top_left_value = top_right_value + size - 1
    bottom_left_value = top_left_value + size - 1
    bottom_right_value = bottom_left_value + size - 1
    value = bottom_right_value

    if is_prime(top_right_value):
        primes += 1
    if is_prime(top_left_value):
        primes += 1
    if is_prime(bottom_left_value):
        primes += 1
    if is_prime(bottom_right_value):
        primes += 1
    total += 4

    if primes / total < 0.1:
        break

print(size)