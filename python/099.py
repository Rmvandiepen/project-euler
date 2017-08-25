import math

from helpers import st, pt

st()
base_exps = []
with open('files/099_base_exp.txt', 'r') as base_exp_data:
    for line in base_exp_data:
        base, exp = line.split(',')
        base_exps.append((int(base), int(exp)))

x_base = base_exps[0][0]
x_power = base_exps[0][1]
highest_log = x_power * math.log(x_base, 2)
a = 0
for x in range(1, len(base_exps)):
    x_base = base_exps[x][0]
    x_power = base_exps[x][1]
    log = x_power * math.log(x_base, 2)
    if log > highest_log:
        highest_log = log
        a = x
print(a + 1)

pt()
