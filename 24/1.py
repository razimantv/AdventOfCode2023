import numpy as np
import itertools

x1, x2 = 200000000000000, 400000000000000
with open('1.2.in') as file:
    pv = np.array([
        [
            list(map(int, part.split(', ')[:2]))
            for part in line[:-1].split(' @ ')
        ] for line in file
    ])

cnt = 0
for (p1, v1), (p2, v2) in itertools.combinations(pv, 2):
    if v1[0] * v2[1] == v1[1] * v2[0]:
        continue
    dp = p2 - p1
    t1 = (dp[0] * v1[1] - dp[1] * v1[0]) / (v2[1] * v1[0] - v2[0] * v1[1])
    t2 = (dp[0] * v2[1] - dp[1] * v2[0]) / (v2[1] * v1[0] - v2[0] * v1[1])
    r = p2 + t1 * v2
    if t1 >= 0 and t2 >= 0 and x1 <= r[0] <= x2 and x1 <= r[1] <= x2:
        cnt += 1
print(cnt)
