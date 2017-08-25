from helpers import get_prime_factors

digits = 4
target_consecutive = 4
current_consucutive = 0
i = 1
while True:
    pf = set(get_prime_factors(i))
    if len(pf) == digits:
        current_consucutive += 1
        if current_consucutive == target_consecutive:
            break
    else:
        current_consucutive = 0
    i += 1
print(i - (target_consecutive - 1))


