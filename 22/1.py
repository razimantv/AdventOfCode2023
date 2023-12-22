with open('1.2.in') as file:
    cuboids = sorted([
        [
            [int(x) for x in cuboidstr.split(',')]
            for cuboidstr in line[:-1].split('~')
        ] for line in file
    ], key=lambda x: x[0][2])

highest, crucial = {}, {}
for i, cuboid in enumerate(cuboids):
    base = [
        (x, y)
        for x in range(cuboid[0][0], cuboid[1][0] + 1)
        for y in range(cuboid[0][1], cuboid[1][1] + 1)
    ]
    best = [0, set()]
    for xy in base:
        if xy not in highest:
            continue
        h, c = highest[xy]
        if h > best[0]:
            best = [h, set([c])]
        elif h == best[0]:
            best[1].add(c)

    if len(best[1]) == 1:
        crucial[best[1].pop()] = 1
    newh = best[0] + cuboid[1][2] - cuboid[0][2] + 1
    for xy in base:
        highest[xy] = (newh, i)

print(len(cuboids) - len(crucial))
