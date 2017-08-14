from helpers import get_binary_value, is_palindrome

total = 0
for x in range(1, 10 ** 6, 2):
    if is_palindrome(x) and is_palindrome(get_binary_value(x)):
        total += x
print(total)
