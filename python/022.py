import string

names = open('files/022_names.txt', 'r').read()
names = [name[1:-1].lower() for name in names.split(',')]
names = sorted(names)

total = 0
for index, name in enumerate(names):
    name_sum = 0
    for char in name:
        name_sum += (string.ascii_lowercase.index(char) + 1)
    name_score = name_sum * (index + 1)
    total += name_score
print(total)