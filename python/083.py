from helpers import st, pt, time_spend_start, time_spend_end

matrix = {}
with open('files/083_matrix.txt', 'r') as matrix_data:
    y = 0
    for line in matrix_data:
        x = 0
        for number in [int(num) for num in line.split(',')]:
            matrix[x, y] = number
            x += 1
        y += 1

st()
matrix_size = 80

fastest_paths = {
    (0, 0): ({
        'value': matrix[0, 0],
        'path': [(0, 0)]
    })
}

cheapest_locations = {
    (0, 0): matrix[0, 0]
}

allow_right = True
allow_left = True
allow_above = True
allow_below = True


class DoneException(Exception):
    pass


def get_next_cheapest():
    if len(cheapest_locations) == 0:
        raise DoneException()

    cheapest_key = min(cheapest_locations, key=cheapest_locations.get)
    value = cheapest_locations.pop(cheapest_key)
    return cheapest_key, value


i = 0
try:
    while True:
        location, value = get_next_cheapest()
        path = fastest_paths.get(location)['path']

        if allow_right and location[0] < matrix_size - 1:
            time_spend_start('right')
            right_location = (location[0] + 1, location[1])
            right_value = value + matrix[right_location]
            right_fastest_path = fastest_paths.get(right_location)
            if right_fastest_path is None or right_fastest_path['value'] > right_value:
                fastest_paths[right_location] = {
                    'value': right_value,
                    'path': path + [right_location]
                }
                cheapest_locations[right_location] = right_value
            time_spend_end('right')

        if allow_left and location[0] > 0:
            time_spend_start('left')
            left_location = (location[0] - 1, location[1])
            left_value = value + matrix[left_location]
            left_fastest_path = fastest_paths.get(left_location)
            if left_fastest_path is None or left_fastest_path['value'] > left_value:
                fastest_paths[left_location] = {
                    'value': left_value,
                    'path': path + [left_location]
                }
                cheapest_locations[left_location] = left_value
            time_spend_end('left')

        if allow_above and location[1] > 0:
            time_spend_start('above')
            above_location = (location[0], location[1] - 1)
            above_value = value + matrix[above_location]
            above_fastest_path = fastest_paths.get(above_location)
            if above_fastest_path is None or above_fastest_path['value'] > above_value:
                fastest_paths[above_location] = {
                    'value': above_value,
                    'path': path + [above_location]
                }
                cheapest_locations[above_location] = above_value
            time_spend_end('above')

        if allow_below and location[1] < matrix_size - 1:
            time_spend_start('below')
            below_location = (location[0], location[1] + 1)
            below_value = value + matrix[below_location]
            below_fastest_path = fastest_paths.get(below_location)
            if below_fastest_path is None or below_fastest_path['value'] > below_value:
                fastest_paths[below_location] = {
                    'value': below_value,
                    'path': path + [below_location]
                }
                cheapest_locations[below_location] = below_value
            time_spend_end('below')

except DoneException:
    pass

print(fastest_paths[(79, 79)])
pt()
