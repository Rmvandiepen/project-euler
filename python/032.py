pandigital_length = 9
digits_to_contain = [str(i) for i in range(1, pandigital_length + 1)]

pandigital_products = []
for i in range(2, 10 ** (int(pandigital_length / 2) + 1)):
	print(i)
	digits = list(str(i))
	digits_amount = len(digits)

	if digits_amount != len(set(digits)):
		continue
	for j in range(2, 10 ** (int(pandigital_length / 2) + 1)):
		digits += list(str(j))
		if len(digits) != len(set(digits)):
			continue

		product = i * j
		digits += list(str(product))
		if len(digits) != len(set(digits)):
			continue

		if set(digits) == set(digits_to_contain):
			print((i, j, product))
			pandigital_products.append((i, j, product))


print(pandigital_products)

