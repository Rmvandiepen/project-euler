from collections import Counter

concatenated_products = []
digits_to_contain = Counter([str(digit) for digit in range(1, 10)])
for x in range(1, 100000):
    digits = []
    n = 1
    while True:
        digits += list(str(x * n))
        if len(set(digits)) != len(digits):
            break
        elif Counter(digits) == digits_to_contain:
            concatenated_products.append(''.join(digits))
            break
        n += 1

print(sorted(concatenated_products))