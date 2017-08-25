from helpers import is_prime
from collections import Counter

for x in range(1000, 10000 - (3330 * 2)):
    x_2 = x + 3330
    x_3 = x + (2 * 3330)
    if is_prime(x) and is_prime(x_2) and is_prime(x_3) and Counter(list(str(x))) == Counter(list(str(x_2))) and Counter(list(str(x))) == Counter(list(str(x_3))):
        print(str(x) + str(x_2) + str(x_3))
