

def get_prime_numbers_until(highest_number):
    prime_numbers = [True for _ in range(int(highest_number))]
    for x in range(2, int(highest_number ** 0.5)):
        if not prime_numbers[x]:
            continue
        y = 2
        while x * y < highest_number:
            prime_numbers[x * y] = False
            y += 1
    return [i for i, value in enumerate(prime_numbers) if value and i > 1]


def is_prime(number):
    if number % 2 == 0:
        return False
    for num in range(3, int(number ** 0.5), 2):
        if number % num == 0:
            return False
    return True


number = 600851475143
root = number ** 0.5
print(root)
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
