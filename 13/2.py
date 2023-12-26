import numpy as np


def symm(mat, i, m):
    l, r = i - 1, i
    while l >= 0 and r < m:
        if (mat[l] != mat[r]).any():
            return False
        l, r = l - 1, r + 1
    return True


def get(mat):
    m = len(mat)
    ret = []
    for i in range(1, m):
        if symm(mat, i, m):
            ret.append(i)
    return ret


cur = []
tot = 0
with open('1.2.in') as file:
    for line in file:
        if len(line) > 1:
            cur.append(line[:-1])
            continue
        mat = np.array([[c for c in row] for row in cur])
        u0, v0 = get(mat), get(mat.T)
        m, n = mat.shape
        for i in range(m):
            for j in range(n):
                c = mat[i][j]
                mat[i][j] = '.' if c == '#' else '#'
                u, v = get(mat), get(mat.T)
                mat[i][j] = c
                if u and u != u0:
                    x = [uu for uu in u if uu not in u0][0]
                    tot += x * 100
                    break
                elif v and v != v0:
                    x = [vv for vv in v if vv not in v0][0]
                    tot += x
                    break
            else:
                continue
            break
        cur = []

print(tot)
