with open('1.2.in') as file:
    grid = [line[:-1] for line in file]
m, n = len(grid), len(grid[0])

process = {
    'r': [(0, 1), {
        "\\": ['d'], '/': ['u'], '|': ['u', 'd']
    }],
    'l': [(0, -1), {
        '\\': ['u'], '/': ['d'], '|': ['u', 'd']
    }],
    'u': [(-1, 0), {
        '\\': ['l'], '/': ['r'], '-': ['r', 'l']
    }],
    'd': [(1, 0), {
        '\\': ['r'], '/': ['l'], '-': ['r', 'l']
    }]
}


def get(i, j, dir):
    seen = {(i, j, dir)}
    todo = [(i, j, dir)]
    cellsseen = [[0] * n for i in range(m)]
    while todo:
        i, j, dir = todo.pop()
        cellsseen[i][j] = 1
        for nextdir in process[dir][1].get(grid[i][j], [dir]):
            di, dj = process[nextdir][0]
            ii, jj = i + di, j + dj
            if ii < 0 or jj < 0 or ii >= m or jj >= n or (ii, jj, nextdir) in seen:
                continue
            seen.add((ii, jj, nextdir))
            todo.append((ii, jj, nextdir))

    return sum(sum(row) for row in cellsseen)


best = 0
for i in range(m):
    best = max(best, get(i, 0, 'r'), get(i, n-1, 'l'))
for j in range(n):
    best = max(best, get(0, j, 'd'), get(m-1, j, 'u'))
print(best)
