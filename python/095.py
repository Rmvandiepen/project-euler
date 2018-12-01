import copy

from helpers import get_divisables, is_prime, st, pt

longest_chain = 0
longest_chain_min_value = 0

st()

chain_lengths = {}
for num in range(2, int(10 ** 6)):
    if is_prime(num):
        continue
    elif num in chain_lengths:
        continue

    chain = [num]
    divisables_sum = num
    while True:
        divisables = copy.deepcopy(get_divisables(divisables_sum))
        divisables.remove(divisables_sum)
        divisables_sum = int(sum(divisables))

        if divisables_sum > 10 ** 6:
            for chain_num in chain:
                chain_lengths[chain_num] = 0
            break
        elif divisables_sum in chain_lengths:
            for chain_num in chain:
                chain_lengths[chain_num] = 0
            break
        elif divisables_sum in chain:
            chain_start = chain.index(divisables_sum)
            chain_length = len(chain) - chain_start

            for chain_num in chain[chain_start:]:
                # print('adding length', chain, chain_num, chain_length)
                chain_lengths[chain_num] = chain_length
                if chain_length > longest_chain:
                    longest_chain = chain_length
                    longest_chain_min_value = chain_num
                elif chain_length == longest_chain and chain_num < longest_chain_min_value:
                    longest_chain_min_value = chain_num

            break
        elif is_prime(divisables_sum):
            for chain_num in chain:
                chain_lengths[chain_num] = 0
            break

        chain.append(divisables_sum)

print(longest_chain_min_value)
pt()
