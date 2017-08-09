from helpers import get_divisables

num = 1
step = 2
while True:
    if num % 12 == 0 and len(get_divisables(num)) > 500:
        break
    num += step
    step += 1

print(num)