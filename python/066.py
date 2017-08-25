results = {}

for d in range(1, 100):
    if (d ** 0.5).is_integer():
        continue
    y = 1
    while True:
        x = ((d * (y ** 2)) + 1) ** 0.5
        if x.is_integer():
            results[d] = (x, y)
            break
        y += 1

print(results)