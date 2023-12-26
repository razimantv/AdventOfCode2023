from collections import Counter

labels = 'AKQJT98765432'
values = {c: i for i, c in enumerate(labels[::-1])}

hands = []
with open('1.2.in') as file:
    for line in file:
        hand, val = line[:-1].split(' ')
        hands.append([
            sorted(Counter(hand).values(), reverse=True),
            [values[c] for c in hand], int(val)
        ])

print(sum(
    (i + 1) * value
    for i, (_, _, value) in enumerate(sorted(hands))
))
