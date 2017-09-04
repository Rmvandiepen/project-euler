from helpers import get_divisables

num = 1
step = 2
while True:
    divs = get_divisables(num)
    if num % 12 == 0 and len(divs) > 500:
        break
    num += step
    step += 1

print(num, len(divs))