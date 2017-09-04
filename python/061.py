import math


def wortel_formule(a, b, c):
    d = b ** 2 - (4 * a * c)
    plus = ((b * -1) + math.sqrt(d)) / (2 * a)
    minus = ((b * -1) - math.sqrt(d)) / (2 * a)
    return min(minus, plus), max(minus, plus)


def get_triangle_base(num):
    return wortel_formule(1, 1, num * -2)[1]


def get_square_base(num):
    return num ** 0.5


def get_pentagonal_base(num):
    return wortel_formule(3, -1, num * -2)[1]


def get_hexagonal_base(num):
    return wortel_formule(2, -1, num * -1)[1]


def get_heptagonal_base(num):
    return wortel_formule(5, -3, num * -2)[1]


def get_octagonal_base(num):
    return wortel_formule(3, -2, num * -1)[1]


def is_triangle(num):
    a = get_triangle_base(num)
    return int(a) == a


def is_square(num):
    a = get_square_base(num)
    return int(a) == a


def is_pentagonal(num):
    a = get_pentagonal_base(num)
    return int(a) == a


def is_hexagonal(num):
    a = get_hexagonal_base(num)
    return int(a) == a


def is_heptagonal(num):
    a = get_heptagonal_base(num)
    return int(a) == a


def is_octagonal(num):
    a = get_octagonal_base(num)
    return int(a) == a

triangles = []
squares = []
pentagonals = []
hexagonals = []
heptagonals = []
octagonals = []

functions = {
    'triangle': (is_triangle, triangles),
    'square': (is_square, squares),
    'pentagonal': (is_pentagonal, pentagonals),
    'hexagonal': (is_hexagonal, hexagonals),
    'heptagonal': (is_heptagonal, heptagonals),
    'octagonal': (is_octagonal, octagonals)
}
lists = [
    triangles, squares, pentagonals, hexagonals, heptagonals, octagonals
]
cycle_len = 6
valids = ['triangle', 'square', 'pentagonal', 'hexagonal', 'heptagonal', 'octagonal']

for x in range(1000, 10000):
    for function, l in functions.values():
        if function(x):
            l.append(x)


def try_a(cycle, options):
    if len(cycle) == cycle_len:
        return [cycle]

    result = []
    for option in options:
        l = functions[option][1]
        nums = []
        if len(cycle) == 0:
            nums = l
        elif len(cycle) == cycle_len - 1:
            nums = [x for x in l if x % 100 == int(cycle[0] / 100) and int(x / 100) == cycle[-1] % 100]
        else:
            nums = [x for x in l if int(x / 100) == cycle[-1] % 100]
        for y in nums:
            new_options = list(options)
            new_options.remove(option)
            result += try_a(cycle + [y], new_options)
    return result

print(sum(try_a([], valids)[1]))
