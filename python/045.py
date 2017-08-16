highest_triangle = 0
triangle_index = 0

highest_pentagonal = 0
pentagonal_index = 0

highest_hexagonal = 0
hexagonal_index = 0


def get_next_triangle_number():
    global highest_triangle, triangle_index
    triangle_index += 1
    highest_triangle = int(triangle_index * (triangle_index + 1) / 2)


def get_next_pentagonal_number():
    global highest_pentagonal, pentagonal_index
    pentagonal_index += 1
    highest_pentagonal = int(pentagonal_index * (3 * pentagonal_index - 1) / 2)


def get_next_hexagonal_number():
    global highest_hexagonal, hexagonal_index
    hexagonal_index += 1
    highest_hexagonal = int(hexagonal_index * (2 * hexagonal_index - 1))

i = 40755 + 1
while True:
    while i > highest_hexagonal:
        get_next_hexagonal_number()
    i = highest_hexagonal

    while i > highest_triangle:
        get_next_triangle_number()

    while i > highest_pentagonal:
        get_next_pentagonal_number()

    if i == highest_triangle and i == highest_pentagonal and i == highest_hexagonal:
        break
    i += 1
print(i)
