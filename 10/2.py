left = '-J7S'
right = '-LFS'
up = '|LJS'
down = '|7FS'
weights = {'|': 2, 'F': 1, 'J': 1, '-': 0, '7': 3, 'L': 3, 'S': 3}

with open('1.2.in') as file:
    grid = [line[:-1] for line in file]
m, n = len(grid), len(grid[0])

par = {(i, j): (i, j) for i in range(m) for j in range(n)}


def parent(u):
    if par[u] != u:
        par[u] = parent(par[u])
    return par[u]


for i in range(m):
    for j in range(n):
        if grid[i][j] == 'S':
            start = (i, j)
        if i and grid[i-1][j] in down and grid[i][j] in up:
            par[parent((i, j))] = parent((i - 1, j))
        if j and grid[i][j-1] in right and grid[i][j] in left:
            par[parent((i, j))] = parent((i, j - 1))

spar = parent(start)
tot = 0
for i in range(m):
    vert = False
    for j in range(m):
        if parent((i, j)) == spar:
            vert += weights[grid[i][j]]
        elif vert % 4 == 2:
            tot += 1
print(tot)
