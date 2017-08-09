from helpers import is_palindrome

highest_result = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y
        if str(product) == str(product)[::-1] and product > highest_result:
            highest_result = product

print(highest_result)


highest_result = 0
for x in range(100, 1000):
    for y in range(x, 1000):
        highest_result = max(highest_result, is_palindrome(x * y))

print(highest_result)


print(sorted([x * y for x in range(100, 1000) for y in range(x, 1000) if str(x*y) == str(x*y)[::-1]])[-1])
