from helpers import get_divisables

val = 3 / 7
target = 1000000
a = set()
closest = (0, 0)
closest_val = 0

for d in range(2, target):
    d_divisables = set(get_divisables(d))
    for n in range(int(d * closest_val) + 1, int(d * val) + 1):
        n_divisables = set(get_divisables(n))
        if d_divisables.intersection(n_divisables) == {1}:
            value = n / d
            if closest_val < value < val:
                closest = (d, n)
                closest_val = value
print(closest[1])