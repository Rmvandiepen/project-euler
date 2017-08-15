p_max = 1000
max_solutions = (0, 0)
for p in range(1, p_max + 1):
    third_p = p // 3
    half_p = p // 2
    solutions = 0
    for a in range(1, third_p + 1):
        a_square = a ** 2
        for b in range(half_p - a, half_p + 1):
            b_square = b ** 2
            if a + b + ((a_square + b_square) ** 0.5) == p:
                solutions += 1
    if solutions > max_solutions[1]:
        max_solutions = (p, solutions)

print(max_solutions[0])
