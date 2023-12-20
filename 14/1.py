with open('1.2.in') as file:
    grid = [[c for c in line[:-1]] for line in file]

m, n = len(grid), len(grid[0])
grid = [''.join([grid[i][j] for i in range(m)]) for j in range(n)]
m, n = n, m
print(sum(
    m - i
    for row in grid
    for i, c in enumerate(
        '#'.join(
            ''.join(sorted(s, reverse=True))
            for s in row.split('#')
        )
    ) if c == 'O'
))
