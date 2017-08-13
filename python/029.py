result_set = set()
min_val = 2
max_val = 100
for a in range(min_val, max_val + 1):
	for b in range(min_val, max_val + 1):
		result_set.add(a ** b)

result = list(result_set)
result.sort()
print(len(result))