import itertools

from collections import defaultdict

from helpers import is_prime, get_prime_numbers_until, st, pt, time_spend_start, time_spend_end, get_next_prime

st()

working_combos = defaultdict(set)
target = 5
all_primes = []


def get_more_primes():
    global working_combos, all_primes
    all_primes = get_prime_numbers_until(10000)
    all_primes.remove(2)
    all_primes.remove(5)
    for cur_prime in all_primes:
        for prime in list(working_combos.keys()):
            left = int(str(prime) + str(cur_prime))
            right = int(str(cur_prime) + str(prime))
            if is_prime(left) and is_prime(right):
                working_combos[prime].add(cur_prime)
                working_combos[cur_prime].add(prime)
        working_combos[cur_prime] = set()


def get_pos_combos(num, extras):
    result = [extras + [num]]
    for candidate in working_combos[num]:
        if candidate <= num or candidate in extras or not is_extras_valid(candidate, extras):
            continue
        result += get_pos_combos(candidate, extras + [num])
    return result


def is_extras_valid(candidate, extras):
    for e in extras:
        pos = working_combos[e]
        if candidate not in pos:
            return False
    return True

time_spend_start('process_prime')
get_more_primes()
time_spend_end('process_prime')

time_spend_start('valids')
valids = []
for prime in all_primes:
    b = get_pos_combos(prime, [])
    for c in b:
        if len(c) >= target:
            valids.append(c)
time_spend_end('valids')

time_spend_start('minimum')
minimum = (sum(valids[0]), valids[0])
for val in valids:
    if sum(val) < minimum[0]:
        minimum = (sum(val), val)
time_spend_end('minimum')

pt()
print(minimum[0])


