from helpers import is_prime

circular_primes = [2]
end = 10 ** 6
for i in range(3, end, 2):
    str_i = str(i)
    rotations = len(str_i)
    for j in range(rotations + 1):
        if not is_prime(int(str_i)):
            break
        str_i = str_i[1:] + str_i[0]
    else:
        circular_primes.append(i)
    continue

print(len(circular_primes))
