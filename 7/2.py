from collections import Counter

labels = 'AKQT98765432J'
values = {c: i for i, c in enumerate(labels[::-1])}


def best(hand):
    cards = set(hand)
    if 'J' in cards and len(cards) > 1:
        cards.remove('J')
    else:
        return sorted(Counter(hand).values(), reverse=True)

    for i, c in enumerate(hand):
        if c == 'J':
            return max(best(hand[:i] + cc + hand[i+1:]) for cc in cards)


hands = []
with open('1.2.in') as file:
    for line in file:
        hand, val = line[:-1].split(' ')
        hands.append([
            best(hand), [values[c]for c in hand], int(val)
        ])

print(sum(
    (i + 1) * value
    for i, (_, _, value) in enumerate(sorted(hands))
))
