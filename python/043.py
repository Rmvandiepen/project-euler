from helpers import st, pt

st()


def add_digit(digits, digits_left):
    digits_amount = len(digits)
    if digits_amount == 4 and not int(''.join(digits[1:4])) % 2 == 0:
        return []
    elif digits_amount == 5 and not int(''.join(digits[2:5])) % 3 == 0:
        return []
    elif digits_amount == 6 and not int(''.join(digits[3:6])) % 5 == 0:
        return []
    elif digits_amount == 7 and not int(''.join(digits[4:7])) % 7 == 0:
        return []
    elif digits_amount == 8 and not int(''.join(digits[5:8])) % 11 == 0:
        return []
    elif digits_amount == 9 and not int(''.join(digits[6:9])) % 13 == 0:
        return []
    elif len(digits) == 10:
        return [int(''.join(digits))] if int(''.join(digits[7:])) % 17 == 0 else []

    posibilities = []
    for digit in digits_left:
        if len(digits) == 0 and digit == '0':
            continue
        left = list(digits_left)
        left.remove(digit)
        posibilities += add_digit(digits + [digit], left)
    return posibilities

posibilities = add_digit([], [str(digit) for digit in range(0, 10)])
print(sum(posibilities))

pt()
