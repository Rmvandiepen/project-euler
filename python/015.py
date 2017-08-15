size = 498
solutions_map = {}


def go_to_path(x, y):
    if (x, y) in solutions_map:
        return solutions_map[(x, y)]

    solutions = 0
    if x == size and y == size:
        return 1
    if x + 1 <= size:
        solutions += go_to_path(x + 1, y)
    if y + 1 <= size:
        solutions += go_to_path(x, y + 1)
    solutions_map[(x, y)] = solutions
    return solutions

solutions = go_to_path(0, 0)
print(solutions)
