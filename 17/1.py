import queue

with open('1.2.in') as file:
    grid = [line[:-1] for line in file]
m, n = len(grid), len(grid[0])

dr = {
    'r': (0, 1),
    'l': (0, -1),
    'u': (-1, 0),
    'd': (1, 0)
}

start = (0, 0, 'r', 0)
distmap = {start: 0}
pq = queue.PriorityQueue()
pq.put((0, start))

while pq:
    dist, state = pq.get()
    i, j, dir, steps = state
    if i == m-1 and j == n-1:
        print(dist, state)
        break
    if dist > distmap[state]:
        continue
    for newdir in (dir if steps < 3 else '') + ('ud' if dir in 'lr' else 'lr'):
        di, dj = dr[newdir]
        ii, jj = i + di, j + dj
        if ii < 0 or ii >= m or jj < 0 or jj >= n:
            continue
        newsteps = steps + 1 if dir == newdir else 1
        newstate = (ii, jj, newdir, newsteps)
        newdist = dist + int(grid[ii][jj])
        if newstate in distmap:
            if distmap[newstate] <= newdist:
                continue
            else:
                pq.queue.remove((distmap[newstate], newstate))
        distmap[newstate] = newdist
        pq.put((newdist, newstate))
