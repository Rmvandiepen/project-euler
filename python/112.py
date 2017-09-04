i = 1
bouncy = 0
not_bouncy = 0
target = 99

while True:
    str_i = str(i)
    digits = list(str_i)

    if sorted(digits) == digits or sorted(digits) == list(reversed(digits)):
        not_bouncy += 1
    else:
        bouncy += 1
    percentage = bouncy / (not_bouncy + bouncy) * 100
    if percentage >= target:
        break
    i += 1
print(i)
