digits = [
    'zero', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]


def getnum(s):
    d1 = min([
        (i, di)
        for di, d in enumerate(digits)
        if (i := s.find(d)) != -1
    ])[1] % 10
    d2 = min([
        (i, di)
        for di, d in enumerate(digits)
        if (i := s[::-1].find(d[::-1])) != -1
    ])[1] % 10
    return d1 * 10 + d2


tot = 0
with open('1.2.in') as file:
    for line in file:
        tot += getnum(line)

print(tot)
