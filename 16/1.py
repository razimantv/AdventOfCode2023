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
seen = {(0, 0, 'r')}
todo = [(0, 0, 'r')]
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

print(sum(sum(row) for row in cellsseen))
