galaxies, colseen, rowseen = [], {}, {}
with open('1.2.in') as file:
    for i, line in enumerate(file):
        for j, c in enumerate(line):
            if c == '#':
                galaxies.append((i, j))
                rowseen[i] = 1
                colseen[j] = 1

m, n = max(rowseen) + 1, max(colseen) + 1
rowpos, colpos = [0] * m, [0] * n
for i in range(1, m):
    rowpos[i] = rowpos[i-1] + (1 if i-1 in rowseen else 1000000)
for i in range(1, m):
    colpos[i] = colpos[i-1] + (1 if i-1 in colseen else 1000000)

tot = 0
for i, (x1, y1) in enumerate(galaxies):
    for x2, y2 in galaxies[:i]:
        tot += abs(rowpos[x1] - rowpos[x2]) + abs(colpos[y1] - colpos[y2])
print(tot)
