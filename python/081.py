from helpers import st, pt

matrix = {}
with open('files/081_matrix.txt', 'r') as matrix_data:
    y = 0
    for line in matrix_data:
        x = 0
        for number in [int(num) for num in line.split(',')]:
            matrix[x, y] = number
            x += 1
        y += 1

st()
matrix_size = 80

fastest_paths = {}
x = 0
fastest_paths[0, 0] = matrix[0, 0]
for y in range(1, matrix_size):
    fastest_paths[x, y] = fastest_paths[x, y - 1] + matrix[x, y]

for x in range(1, matrix_size):
    for y in range(matrix_size):
        new_value = fastest_paths[x - 1, y] + matrix[x, y]
        fastest_paths[x, y] = new_value
    for y in range(1, matrix_size):
        new_value = fastest_paths[x, y - 1] + matrix[x, y]
        fastest_paths[x, y] = min(fastest_paths[x, y], new_value)

print(fastest_paths[matrix_size - 1, matrix_size - 1])

pt()
