import numpy as np


def symm(mat, i, m):
    l, r = i - 1, i
    while l >= 0 and r < m:
        if (mat[l] != mat[r]).any():
            return False
        l, r = l - 1, r + 1
    return True


def get(mat):
    m, tot = len(mat), 0
    for i in range(1, m):
        if symm(mat, i, m):
            tot += i
    return tot


cur = []
tot = 0
with open('1.2.in') as file:
    for line in file:
        if len(line) > 1:
            cur.append(line[:-1])
            continue
        mat = np.array([[c for c in row] for row in cur])
        tot += get(mat) * 100 + get(mat.T)
        cur = []
print(tot)
