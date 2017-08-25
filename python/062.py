from collections import defaultdict

multiples = defaultdict(list)
target = 5
i = 1
while True:
    cube = i ** 3
    cube_str = ''.join([str(digit) for digit in sorted(list(str(cube)))])
    multiples[cube_str].append((i, cube))
    if len(multiples[cube_str]) >= target:
        break
    i += 1
print(multiples[cube_str][0][1])
