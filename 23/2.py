with open('1.2.in') as file:
    grid = [line[:-1] for line in file]
m, n = len(grid), len(grid[0])
dr = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def neighbours(i, j):
    return [
        (ii, jj) for di, dj in dr
        if (ii := i + di) >= 0 and (jj := j + dj) > 0 and ii < m and jj < n
        and grid[ii][jj] != '#'
    ]


vertices = [(0, 1), (m - 1, n - 2)] + [
    (i, j) for i in range(m) for j in range(n)
    if grid[i][j] != '#' and len(neighbours(i, j)) > 2
]
vertmap = {vertex: u for u, vertex in enumerate(vertices)}


def nextvertex(u, v):
    dist = 1
    while u not in vertmap:
        dist += 1
        u, v = [w for w in neighbours(*u) if w != v][0], u
    return vertmap[u], dist


adjlist = {
    u: [nextvertex((ii, jj), (i, j)) for ii, jj in neighbours(i, j)]
    for u, (i, j) in enumerate(vertices)
}
seen = set()


def longest(u):
    if u == 1:
        return 0
    seen.add(u)
    ret = -1
    for v, dist in adjlist[u]:
        if v not in seen and (newdist := longest(v)) != -1:
            ret = max(ret, newdist + dist)
    seen.remove(u)
    return ret


print(longest(0))
