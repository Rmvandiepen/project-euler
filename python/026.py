
def get_recuring_cycle(base, divider):
    cycle = ''
    numbers_tried = []
    left = base
    while True:
        # print(left, cycle, numbers_tried)
        if left in numbers_tried:
            return cycle[1:]
        numbers_tried.append(left)
        fits = left // divider
        left -= fits * divider
        cycle += str(fits)
        left *= 10

highest = (0, 0)
for i in range(1, 1000 + 1):
    recuring_cycle = get_recuring_cycle(1, i)
    if len(recuring_cycle) > highest[1]:
        highest = (i, len(recuring_cycle))
print(highest)
