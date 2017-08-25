print(sum([x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0]))

total = 0
i = 1
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        total = total + i
        print(i, total)
    # if i % 5 == 0:
    #     print(i)
    # print(i)
    i+=1
print(total)