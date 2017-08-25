from helpers import is_palindrome

lychrel_numbers = {}


def reverse(num):
    return int(str(num)[::-1])


for x in range(1, 10000):
    def is_lychrel_number(num, iterations=0):
        if num in lychrel_numbers:
            return lychrel_numbers[num]

        new_num = num + reverse(num)
        if is_palindrome(new_num):
            is_lychrel = False
        elif iterations >= 50:
            is_lychrel = True
        else:
            is_lychrel = is_lychrel_number(new_num, iterations + 1)
        if num < 10000:
            lychrel_numbers[num] = is_lychrel
        return is_lychrel
    x = is_lychrel_number(x)

print(len([x for x in lychrel_numbers.values() if x]))


