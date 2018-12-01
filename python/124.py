from helpers import get_divisables, is_prime, st, pt

rad_ns = {}
st()
for n in range(1, 100000 + 1):
    divisables = get_divisables(n)
    rad_n = 1
    for divisable in divisables:
        if is_prime(divisable):
            rad_n *= divisable
    rad_ns[n] = rad_n


sorted_stuff = sorted(rad_ns, key=rad_ns.__getitem__)
print(sorted_stuff[10000 - 1])
pt()
