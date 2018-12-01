from decimal import Decimal, getcontext

from helpers import st, pt, time_spend_start, time_spend_end

fibs = {1: Decimal(1), 2: Decimal(1)}

# for x in range(3, 30000):
x = 2
pow = 1

getcontext().prec = 23000000
getcontext().Emin = -999999999
getcontext().Emax = 999999999

st()
while True:
    x += 1
    if x == 10 ** pow:
        print(f'At {x}')
        pow += 1
        if pow == 7:
            break

    time_spend_start('next_fib')
    fib = fibs[x - 1] + fibs[x - 2]
    fibs[x] = fib
    fibs.pop(x - 2)
    time_spend_end('next_fib')

    # print(x, fib)
    start = end = False

    time_spend_start('to_string')
    str_fib = str(fib)
    time_spend_end('to_string')

    time_spend_start('trunc_head')
    head = str_fib[:9]
    time_spend_end('trunc_head')

    time_spend_start('sort_head')
    sorted_head = sorted(head)
    time_spend_end('sort_head')

    time_spend_start('joined_head')
    joined_head = ''.join(sorted_head)
    time_spend_end('joined_head')
    # print(joined_head)
    if joined_head != '123456789':
        continue

    print(f'{x} starts pandigital, current length: {len(str_fib)}')
    tail = str_fib[-9:]
    sorted_tail = sorted(tail)
    joined_tail = ''.join(sorted_tail)
    if joined_tail != '123456789':
        continue

    print(f'{x} starts and ends pandigital')
    break

pt()