import string

triangle_numbers = []
highest_triangle_number = 0
highest_triangle_number_index = 0


def get_triangle_number_for_index(index):
    return 0.5 * index * (index + 1)


def calculate_triangle_until(number):
    global highest_triangle_number, highest_triangle_number_index
    while highest_triangle_number < number:
        highest_triangle_number_index += 1
        highest_triangle_number = get_triangle_number_for_index(highest_triangle_number_index)
        triangle_numbers.append(highest_triangle_number)


def calculate_word_value(word):
    word_value = 0
    for char in word:
        word_value += (string.ascii_lowercase.index(char) + 1)
    return word_value

words = open('files/042_words.txt', 'r').read()
words = [word[1:-1].lower() for word in words.split(',')]

triangle_words = []
for word in words:
    word_value = calculate_word_value(word)
    if word_value > highest_triangle_number:
        calculate_triangle_until(word_value)

    if word_value in triangle_numbers:
        triangle_words.append(word)

print(len(triangle_words))
