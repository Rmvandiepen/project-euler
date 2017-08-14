from helpers import is_prime, product

highest_combo = (0, 0, 0)
for a in range(-999, 1000):
    for b in range(-1000, 1001):
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

print(product([highest_combo[0], highest_combo[1]]))


