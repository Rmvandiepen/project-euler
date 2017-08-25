import operator
from collections import defaultdict

file_data = open('files/059_cipher.txt', 'r').read()
message = [int(digit) for digit in file_data.split(',')]


def encrypt(message, password):
    key = [ord(char) for char in password]
    result = []
    for index, digit in enumerate(message):
        result += [digit ^ (key[index % len(key)])]
    return result


def find_key(message, look_for, key_length=3):
    space_digit = ord(look_for)
    digits = []
    for offset in range(key_length):
        i = offset
        a = defaultdict(int)
        while i < len(message):
            key = space_digit ^ message[i]
            a[key] += 1
            i += key_length
        digits.append(max(a.items(), key=operator.itemgetter(1))[0])
    return ''.join([chr(digit) for digit in digits])


result = encrypt(message, find_key(message, ' '))
text = ''.join([chr(digit) for digit in result])

print(sum([ord(char) for char in text]))
