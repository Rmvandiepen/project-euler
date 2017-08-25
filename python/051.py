import itertools

from helpers import get_prime_numbers_until, time_spend_start, time_spend_end, st, pt, is_prime

st()

# time_spend_start('primes')
primes = get_prime_numbers_until(1000000)
prime_set = set(primes)
# time_spend_end('primes')


def replace_str_index(text, index=0, replacement=''):
    return '%s%s%s' % (text[:index], replacement, text[index+1:])

target = 8
primes_checked = []
for prime in primes:
    str_prime = str(prime)
    # time_spend_start('combinations')
    length = len(str_prime)
    spots = range(length - 1)
    combinations = []
    for x in range(1, length):
        combinations += list(itertools.combinations(spots, x))
    # time_spend_end('combinations')

    for combination in combinations:
        valid = True
        digit = str_prime[combination[0]]
        for posititon in combination:
            if digit != str_prime[posititon]:
                valid = False
        if not valid:
            continue
        i = 0
        for digit in range(1 if 0 in combination else 0, 10):
            if 10 - digit + i < target:
                break
            str_digit = str(digit)
            new_value = str_prime
            # time_spend_start('tag1')
            for posititon in combination:
                new_value = replace_str_index(new_value, posititon, str_digit)
            # time_spend_end('tag1')

            # time_spend_start('tag2')
            if int(new_value) in prime_set:
                i += 1
            # time_spend_end('tag2')
        if i >= target:
            break
    else:
        continue
    break

print(prime)

pt()