from helpers import st, pt

num_worth = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}


def parse_file():
    results = []
    with open('files/089_roman.txt', 'r') as base_exp_data:
        for line in base_exp_data:
            if line[-1] == '\n':
                line = line[:-1]
            results.append(line)
    return results


def get_number_from_roman(roman):
    location = 0

    result = 0
    while location < len(roman):
        current_char = roman[location]
        value = num_worth[current_char]
        if location < len(roman) - 1 and value < num_worth[roman[location + 1]]:
            location += 1
            value = num_worth[roman[location]] - value
        result += value
        location += 1
    return result


def get_roman_from_number(number):
    roman = ''
    while number > 0:
        for roman_key, value in num_worth.items():
            if number >= value:
                roman += roman_key
                number -= value
                break
    return roman


romans = parse_file()
st()
char_count = 0
for roman in romans:
    number = get_number_from_roman(roman)
    roman_after = get_roman_from_number(number)
    chars_saved = len(roman) - len(roman_after)
    # if chars_saved != 0:
    #     print(roman, number, roman_after, (len(roman) - len(roman_after)))
    char_count += chars_saved

print(char_count)
pt()
