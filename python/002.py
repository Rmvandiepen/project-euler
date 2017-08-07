result = 0
first_num = 1
second_num = 2
while second_num <= 4000000:
    result += second_num if second_num % 2 == 0 else 0
    new_second = first_num + second_num
    first_num = second_num
    second_num = new_second
print(result)