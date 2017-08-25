pandigital_length = 9
digits_to_contain = [str(i) for i in range(1, pandigital_length + 1)]

pandigital_products = []
for i in range(2, 100):
    i_digits = list(str(i))
    digits_amount = len(i_digits)

    if digits_amount != len(set(i_digits)):
        continue
    digits_needed = 4 if digits_amount == 1 else 3
    for j in range(10 ** (digits_needed - 1), 10 ** digits_needed):
        product = i * j

        digits = i_digits + list(str(j)) + list(str(product))
        if len(digits) != len(set(digits)):
            continue

        if set(digits) == set(digits_to_contain):
            pandigital_products.append((i, j, product))


unique_products = set([product for i, j, product in pandigital_products])
print(sum(unique_products))
