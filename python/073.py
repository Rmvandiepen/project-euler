from helpers import get_divisables

minimum = 1 / 3
maximum = 1 / 2
target = 12000
a = set()
closest = (0, 0)
closest_val = 0
count = 0
for d in range(2, target + 1):
    d_divisables = set(get_divisables(d))
    for n in range(int(d * minimum) + 1, int(d * maximum) + 1):
        n_divisables = set(get_divisables(n))
        if d_divisables.intersection(n_divisables) == {1}:
            value = n / d
            if minimum < value < maximum:
                count += 1
print(count)