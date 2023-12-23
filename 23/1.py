import sys
sys.setrecursionlimit(10000)

with open('1.2.in') as file:
    grid = [line[:-1] for line in file]
m, n = len(grid), len(grid[0])
seen = set()
dr = {'v': (1, 0), '>': (0, 1), '^': (-1, 0), '<': (0, -1)}


def longest(i, j):
    if (i, j) == (m - 1, n - 2):
        return 1
    seen.add((i, j))
    ret = 0
    for c, (di, dj) in dr.items():
        if grid[i][j] not in ('.', c):
            continue
        ii, jj = i + di, j + dj
        if (
            ii < 0 or ii >= m or jj < 0 or jj >= n
        ) or grid[ii][jj] == '#' or (ii, jj) in seen:
            continue
        child = longest(ii, jj)
        if child:
            ret = max(ret, 1 + child)
    seen.remove((i, j))
    return ret


print(longest(0, 1) - 1)
