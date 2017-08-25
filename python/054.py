from collections import defaultdict

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

b = []
with open('files/054_poker.txt', 'r') as fp:
    for line in fp:
        if line[-1] == '\n':
            line = line[:-1]
        cards = line.split(' ')
        b.append((cards[:5], cards[5:]))


def is_highest_card(cards):
    numbers = defaultdict(int)
    for card in cards:
        value = card_values[card[0]]
        numbers[value] += 1
    highest_cards = list(reversed(sorted([number for number, times in numbers.items() if times == 1])))
    if not len(highest_cards) == 5:
        return False, 0
    score = 0
    for i in range(0, len(highest_cards)):
        score += highest_cards[i] * (14 ** (4 - i))
    return True, score


def is_full_house(cards):
    numbers = defaultdict(int)
    for card in cards:
        value = card_values[card[0]]
        numbers[value] += 1
    three_of_a_kinds = [number for number, times in numbers.items() if times == 3]
    pairs = [number for number, times in numbers.items() if times == 2]
    full_house = three_of_a_kinds and pairs
    if not full_house:
        return False, 0
    return True, three_of_a_kinds[0] * 14 + pairs[0]


def is_three_of_a_kind(cards):
    numbers = defaultdict(int)
    for card in cards:
        value = card_values[card[0]]
        numbers[value] += 1
    three_of_a_kinds = [number for number, times in numbers.items() if times == 3]
    highest_cards = list(reversed(sorted([number for number, times in numbers.items() if times == 1])))
    if not three_of_a_kinds:
        return False, 0
    return True, three_of_a_kinds[0] * (14 ** 2) + highest_cards[0] * 14 + highest_cards[1]


def is_two_pairs(cards):
    numbers = defaultdict(int)
    for card in cards:
        value = card_values[card[0]]
        numbers[value] += 1
    pairs = list(reversed(sorted([number for number, times in numbers.items() if times == 2])))
    highest_cards = list(reversed(sorted([number for number, times in numbers.items() if times == 1])))
    if not len(pairs) == 2:
        return False, 0
    return True, pairs[0] * (14 ** 2) + pairs[1] * 14 + highest_cards[0]


def is_pairs(cards):
    numbers = defaultdict(int)
    for card in cards:
        value = card_values[card[0]]
        numbers[value] += 1
    pairs = [number for number, times in numbers.items() if times == 2]
    highest_cards = list(reversed(sorted([number for number, times in numbers.items() if times == 1])))
    if not len(pairs) == 1:
        return False, 0
    return True, pairs[0] * (14 ** 3) + highest_cards[0] * (14 ** 2) + highest_cards[1] * 14 + highest_cards[2]


def is_four_of_a_kind(cards):
    numbers = defaultdict(int)
    for card in cards:
        value = card_values[card[0]]
        numbers[value] += 1
    four_of_a_kinds = [number for number, times in numbers.items() if times == 5]
    highest_cards = [number for number, times in numbers.items() if times == 1]
    four_of_a_kind = four_of_a_kinds
    if not four_of_a_kind:
        return False, 0
    return True, four_of_a_kinds[0] * 14 + highest_cards[0]


def is_royal_flush(cards):
    straight, start = is_straight(cards)
    return is_flush(cards) and straight and start == 10, 0


def is_straight_flush(cards):
    straight, start = is_straight(cards)
    return is_flush(cards) and straight, start


def is_flush(cards):
    colors = set([card[1] for card in cards])
    values = list(reversed(sorted(set([card_values[card[0]] for card in cards]))))
    score = 0
    for i in range(0, len(values)):
        score += values[i] * (14 ** 4 - i)
    return len(colors) == 1, score


def is_straight(cards):
    values = [card_values[card[0]] for card in cards]
    return sorted(values) == list(range(min(values), max(values) + 1)), min(values)

exec_order = [is_royal_flush, is_straight_flush, is_four_of_a_kind, is_full_house, is_flush, is_straight, is_three_of_a_kind, is_two_pairs, is_pairs, is_highest_card]


def get_hand_score(cards):
    for index, a in enumerate(exec_order):
        is_match, score = a(cards)
        if is_match:
            return (10 - index, score)
    return 0


def get_winner(hand1, hand2):
    if hand1[0] > hand2[0] or (hand1[0] == hand2[0] and hand1[1] > hand2[1]):
        return 1
    return 2

player_1_wins = 0
for c in b:
    hand_1 = get_hand_score(c[0])
    hand_2 = get_hand_score(c[1])
    winner = get_winner(hand_1, hand_2)
    if winner == 1:
        player_1_wins += 1

print(player_1_wins)
