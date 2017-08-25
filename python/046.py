from helpers import is_prime, get_next_prime

i = 3
while True:
    i += 2
    # print('i', i)
    if is_prime(i):
        continue
    prime = 2
    valid = False
    while not valid:
        # print('prime', prime)
        for x in range(1, int((i / 2) ** 0.5) + 1):
            # print('x', x, prime + (2 * (x ** 2)))
            if prime + (2 * (x ** 2)) == i:
                valid = True
                break
        prime = get_next_prime(prime)
        if prime >= i:
            break
    if not valid:
        break
print(i)
