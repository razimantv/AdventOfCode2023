with open('1.2.in') as file:
    parts = [line[:-1].split(',') for line in file][0]


def hash(s):
    ret = 0
    for c in s:
        ret = ((ret + ord(c)) * 17) & 255
    return ret


boxes = [[] for _ in range(256)]
for part in parts:
    if part[-1] == '-':
        lens = part[:-1]
        box = boxes[hash(lens)]
        for i, (l, v) in enumerate(box):
            if l == lens:
                box.pop(i)
                break
    else:
        lens = part[:-2]
        val = int(part[-1])
        box = boxes[hash(lens)]
        for i, (l, v) in enumerate(box):
            if l == lens:
                box[i] = (lens, val)
                break
        else:
            box.append((lens, val))

print(sum(
    (b + 1) * (i + 1) * val
    for b, box in enumerate(boxes)
    for i, (lens, val) in enumerate(box)
))
