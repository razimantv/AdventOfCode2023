grid = []
with open('1.2.in') as file:
    for i, line in enumerate(file):
        if (j := line.find('S')) != -1:
            positions = [(i, j)]
            line = line[:j] + '.' + line[j+1:]
        grid.append(line[:-1])
m, n = len(grid), len(grid[0])

neigh = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for round in range(64):
    next = set()
    for i, j in positions:
        for di, dj in neigh:
            ii, jj = i + di, j + dj
            if (
                ii >= 0 and jj >= 0 and ii < m and jj < n
            ) and grid[ii][jj] == '.' and (ii, jj) not in next:
                next.add((ii, jj))
    positions = next
print(len(positions))
