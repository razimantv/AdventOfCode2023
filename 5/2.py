def getmap(filename):
    with open(filename) as file:
        return [
            [int(x) for x in line[:-1].split(' ')]
            for line in file
        ]


def pieces(map, ranges):
    ret = []
    for d, s, l in map:
        newranges = []
        for start, end in ranges:
            a = max(s, start)
            b = min(s + l - 1, end)
            if a <= b:
                ret.append((a + d - s, b + d - s))
                if start < a:
                    newranges.append((start, a - 1))
                if end > b:
                    newranges.append((b + 1, end))
            else:
                newranges.append((start, end))
        ranges = newranges

    return ret + ranges


maps = [
    getmap(f'1.2.{i}.in')
    for i in range(1, 8)
]


def work(ranges):
    for map in maps:
        ranges = pieces(map, ranges)
    return min([range[0] for range in ranges])


s = '3943078016 158366385 481035699 103909769 3553279107 15651230 3322093486 189601966 2957349913 359478652 924423181 691197498 2578953067 27362630 124747783 108079254 1992340665 437203822 2681092979 110901631'
s = [int(x) for x in s.split(' ')]
ranges = [(s[i], s[i] + s[i+1] - 1) for i in range(0, len(s), 2)]
print(work(ranges))
