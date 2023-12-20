with open('1.2.in') as file:
    parts = [line[:-1].split(',') for line in file][0]


def hash(s):
    ret = 0
    for c in s:
        ret = ((ret + ord(c)) * 17) & 255
    return ret


print(sum([hash(s) for s in parts]))
