from helpers import get_factorial

known = {
    169: 3,
    871: 2,
    872: 2,
    1454: 3,
    363601: 3,
    45361: 2,
    45362: 2
}
target = 1000000


def get_chain(number):
    if number in known:
        return known[number]
    new_value = sum([get_factorial(int(digit)) for digit in str(number)])
    if number == new_value:
        known[number] = 0
        return get_chain(number)
    chain_number = get_chain(new_value) + 1
    known[number] = chain_number
    return chain_number

count = 0
for i in range(3, target):
    if get_chain(i) == 60:
        count += 1
print(count)