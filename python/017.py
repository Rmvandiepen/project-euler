word_map = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

size = 0
for x in range(1, 1000 + 1):
    word = ''
    if x >= 1000:
        thousands = int(x / 1000)
        word += word_map[thousands] + word_map[1000]
        x -= thousands * 1000

    if x >= 100:
        hundreds = int(x / 100)
        word += word_map[hundreds] + word_map[100]
        x -= hundreds * 100
        if x > 0:
            word += 'and'

    if x >= 20:
        tenths = int(x / 10) * 10
        word += word_map[tenths]
        x -= tenths

    if x > 0:
        word += word_map[x]

    size += len(word)

print(size)
