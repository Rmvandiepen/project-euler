from collections import defaultdict

numbers = open('files/079_keylog.txt', 'r').read()
numbers = numbers.split('\n')
result = ''
while len(numbers):
    digit_locations = defaultdict(set)
    for number in numbers:
        for index, digit in enumerate(number):
            digit_locations[digit].add(index)

    for digit, locations in digit_locations.items():
        if locations == set([0]):
            result += digit
            for index, number in enumerate(numbers):
                number = ''.join([char for char in number if not char == digit])
                numbers[index] = number
    numbers = [number for number in numbers if len(number)]

print(result)