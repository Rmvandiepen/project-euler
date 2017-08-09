from helpers import get_prime_numbers_until

number = 600851475143
root = number ** 0.5
prime_numbers = get_prime_numbers_until(int(root))
result = 0
for prime_number in reversed(prime_numbers):
    if number % prime_number == 0:
        result = prime_number
        break

# for num in reversed(range(2, int(number ** .5))):
#     if number % num == 0:
#         if is_prime(num):
#             result = num
#             break
print(result)
