import numpy as np
from sage.all import var, solve, show

with open('1.2.in') as file:
    pv = np.array([
        [
            list(map(int, part.split(', ')))
            for part in line[:-1].split(' @ ')
        ] for line in file
    ])


r = [var(f'r{i}') for i in range(3)]
v = [var(f'v{i}') for i in range(3)]
t = [var(f't{i}') for i in range(3)]
eqs = [
    pv[i, 0, j] + pv[i, 1, j] * t[i] == r[j] + v[j] * t[i]
    for i in range(3) for j in range(3)
]
S = solve(eqs, r + v + t)
show(S)
print(sum(ri.substitute(S[0]) for ri in r))
