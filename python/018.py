pyramid = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]
clean_up = {}
highest_routes = {(0, 0): 0}
y = 1
while y < len(pyramid):
    for x in range(len(pyramid[y])):
        position = (y, x)
        prev_y = y - 1
        if x - 1 >= 0:
            prev_x = x - 1
            prev_pos = (prev_y, prev_x)
            num = highest_routes[prev_pos]
            num += pyramid[prev_y][prev_x]
            if position not in highest_routes or highest_routes[position] < num:
                highest_routes[position] = num
        if x <= len(pyramid[prev_y]) - 1:
            prev_x = x
            prev_pos = (prev_y, prev_x)
            num = highest_routes[prev_pos]
            num += pyramid[prev_y][prev_x]
            if position not in highest_routes or highest_routes[position] < num:
                highest_routes[position] = num

    highest_routes = {
        key: value for key, value in highest_routes.items() if key[0] == y
    }
    y += 1

highest_sum = 0
for key, value in highest_routes.items():
    sum_value = value + pyramid[key[0]][key[1]]
    highest_sum = max(highest_sum, sum_value)
print(highest_sum)
