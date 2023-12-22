from collections import defaultdict
import queue

grid = []
with open('1.2.in') as file:
    for i, line in enumerate(file):
        if (j := line.find('S')) != -1:
            start = (i, j)
            line = line[:j] + '.' + line[j+1:]
        grid.append(line[:-1])
L = len(grid)
C = L // 2

neigh = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def distlist(i, j):
    seen = {(i, j)}
    dists = defaultdict(int)
    dists[0] = 1
    bfsq = queue.Queue()
    bfsq.put((0, i, j))
    while not bfsq.empty():
        dist, i, j = bfsq.get()
        for di, dj in neigh:
            ii, jj = i + di, j + dj
            if (
                ii < 0 or jj < 0 or ii >= L or jj >= L
            ) or grid[ii][jj] == '#' or (ii, jj) in seen:
                continue
            dists[dist + 1] += 1
            seen.add((ii, jj))
            bfsq.put((dist + 1, ii, jj))
    return dists


all_dists = {
    (i, j): distlist(i, j)
    for i in [0, C, L-1] for j in [0, C, L-1]
}

steps, tot = 26501365, 0

# Centre
tot += sum(
    v for k, v in all_dists[(C, C)].items()
    if (steps - k) % 2 == 0
)

# Axes
for startpos in [(0, C), (C, 0), (L-1, C), (C, L-1)]:
    distdict = all_dists[startpos]
    startdist_0, maxdist = C + 1, max(distdict)
    i_full_max = (steps - maxdist - startdist_0) // L + 1
    oddcnt = (i_full_max + 1) // 2
    evencnt = i_full_max - oddcnt
    tot += sum(
        v * (oddcnt if (steps - k - startdist_0) % 2 == 0 else evencnt)
        for k, v in distdict.items()
    )

    i = i_full_max
    while (startdist := startdist_0 + i * L) <= steps:
        tot += sum(
            v for k, v in distdict.items()
            if k + startdist <= steps and (steps - k - startdist) % 2 == 0
        )
        i += 1

# Quadrants
for startpos in [(0, 0), (0, L-1), (L-1, 0), (L-1, L-1)]:
    distdict = all_dists[startpos]
    startdist_0, maxdist = L + 1, max(distdict)
    i_full_max = (steps - maxdist - startdist_0) // L + 1
    oddcnt = ((i_full_max + 1) // 2) ** 2
    evencnt = (i_full_max * (i_full_max + 1)) // 2 - oddcnt
    tot += sum(
        v * (oddcnt if (steps - k - startdist_0) % 2 == 0 else evencnt)
        for k, v in distdict.items()
    )
    i = i_full_max
    while (startdist := L + 1 + i * L) < steps:
        tot += (i + 1) * sum(
            v for k, v in distdict.items()
            if k + startdist <= steps and (steps - k - startdist) % 2 == 0
        )
        i += 1
print(tot)
