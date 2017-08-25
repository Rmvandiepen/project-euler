# end_results = {}
# i = 1
# for i in range(1, 10 ** 7):
#     numbers = [i]
#     loops = 1
#     while i not in [1, 89]:
#         if i in end_results:
#             i = end_results[i]
#             break
#
#         i = sum([int(digit) ** 2 for digit in list(str(i))])
#         numbers.append(i)
#         loops += 1
#
#     for num in numbers:
#         end_results[num] = i
# print(len([num for num, x in end_results.items() if x == 89]))


from itertools import combinations_with_replacement as cwr

def digit_sq_sum(n):
    return sum([int(i) ** 2 for i in str(n)])

ends = []
factorials = [1,1,2,6,24,120,720,5040]

for i in range(1,163):
    j = i
    while j not in [1,89]:
        j = digit_sq_sum(j)
    ends.append(j)

for i in range(163,568):
    ends.append(ends[digit_sq_sum(i)-1])

count = 0
end_in_89 = [i+1 for i,n in enumerate(ends) if n == 89]

for i in cwr(range(10),7):
    if sum([k**2 for k in i]) in end_in_89:
        no_of_permutations = 5040
        for j in range(10):
            no_of_permutations //= factorials[i.count(j)]
        count += no_of_permutations

print(count)