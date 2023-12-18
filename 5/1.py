def getmap(filename):
    with open(filename) as file:
        return [
            [int(x) for x in line[:-1].split(' ')]
            for line in file
        ]


def find(map, x):
    for d, s, l in map:
        if s <= x < s + l:
            return d + x - s
    return x


maps = [
    getmap(f'1.2.{i}.in')
    for i in range(1, 8)
]


def work(x):
    for map in maps:
        x = find(map, x)
    return x


print(min([
    work(int(x))
    for x in '3943078016 158366385 481035699 103909769 3553279107 15651230 3322093486 189601966 2957349913 359478652 924423181 691197498 2578953067 27362630 124747783 108079254 1992340665 437203822 2681092979 110901631'.split(' ')
]))
