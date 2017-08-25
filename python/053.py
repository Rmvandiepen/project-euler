from helpers import calculate_combinatorics

total = 0
for n in range(1, 101):
    for r in range(1, n + 1):
        if calculate_combinatorics(n, r) > 1000000:
            total += 1
print(total)
