matrix = {}
with open('files/082_matrix.txt', 'r') as matrix_data:
    y = 0
    for line in matrix_data:
        x = 0
        for number in [int(num) for num in line.split(',')]:
            matrix[(x, y)] = number
            x += 1
        y += 1

matrix_size = 80

fastest_paths = {}
x = 0
for y in range(matrix_size):
    fastest_paths[x, y] = {
        'value': matrix[x, y], 
        'path': [(x, y)]
    }

for x in range(1, matrix_size):
    for y in range(matrix_size):
        left_cell_data = fastest_paths[x - 1, y]
        value = left_cell_data['value'] + matrix[x, y]
        new_path = left_cell_data['path'] + [(x, y)]
        fastest_paths[x, y] = {
            'value': value, 
            'path': new_path
        }
    for y in range(1, matrix_size):
        upper_cell_data = fastest_paths[x, y - 1]
        value = upper_cell_data['value'] + matrix[x, y]
        new_path = upper_cell_data['path'] + [(x, y)]
        if value < fastest_paths[x, y]['value']:
            fastest_paths[x, y] = {
                'value': value, 
                'path': new_path
            }
    for y in reversed(range(matrix_size - 1)):
        below_cell_data = fastest_paths[x, y + 1]
        value = below_cell_data['value'] + matrix[x, y]
        new_path = below_cell_data['path'] + [(x, y)]
        if value < fastest_paths[x, y]['value']:
            fastest_paths[x, y] = {
                'value': value, 
                'path': new_path
            }

min_path = None
for y in range(matrix_size):
    path_data =  fastest_paths[matrix_size - 1, y]
    if not min_path or path_data['value'] < min_path['value']:
        min_path = {
            'value': path_data['value'], 
            'position': (matrix_size - 1, y)
        }

print(min_path['value'])
