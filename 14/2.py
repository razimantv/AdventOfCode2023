import numpy as np

with open('1.2.in') as file:
    grid = np.array([[c for c in line[:-1]] for line in file])
m, n = grid.shape


def bubble(grid):
    return np.array([
        list(
            '#'.join([
                ''.join(sorted(s, reverse=True))
                for s in ''.join(row).split('#')
            ])
        )
        for row in grid
    ])


flats, flatmap = [], {}
for i in range(10 ** 9):
    grid = bubble(grid.T).T
    grid = bubble(grid)
    grid = bubble(grid[::-1, :].T).T[::-1]
    grid = bubble(grid[:, ::-1])[:, ::-1]

    flat = ''.join([''.join(row) for row in grid])
    if flat in flatmap:
        n1, n2 = flatmap[flat], i
        break
    flatmap[flat] = i
    flats.append(flat)


print(sum(
    m - i // n
    for i, c in enumerate(flats[n1 + (10 ** 9 - 1 - n1) % (n2 - n1)])
    if c == 'O'
))
