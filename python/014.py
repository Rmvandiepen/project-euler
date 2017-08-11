
chain_lengths = {1: 1}


def get_chain_length(number):
    if number in chain_lengths:
        return chain_lengths[number]
    chain_length = get_chain_length(3 * number + 1 if number % 2 else number / 2) + 1
    chain_lengths[number] = chain_length
    return chain_length


longest_chain = (0, 0)
for x in range(1, 1000000):
    length = get_chain_length(x)
    if length > longest_chain[1]:
        longest_chain = (x, length)
print(longest_chain)
