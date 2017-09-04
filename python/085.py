target = 2000000
closest = (0, 0, 2000000)
for width in range(1, 1999):
    for height in range(1, 1999):
        squares = 0
        for x in range(1, width + 1):
            for y in range(1, height + 1):
                squares += ((width - x) + 1) * ((height - y) + 1)
        closeness = abs(target - squares)
        if closeness < closest[2]:
            closest = (width, height, closeness)
        if squares > target:
            break
print(closest[0] * closest[1])
