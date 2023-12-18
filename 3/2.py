with open('1.2.in') as file:
    grid = [line[:-1] for line in file]

nums = []
m, n = len(grid), len(grid[0])
for i, line in enumerate(grid):
    left = 0
    while left < n:
        if not line[left].isdigit():
            left += 1
            continue

        right = left + 1
        while right < n and line[right].isdigit():
            right += 1

        nums.append((i, left, right, int(line[left:right])))
        left = right


def hassymbol(s):
    for c in s:
        if c != '.' and not c.isdigit():
            return True
    return False


def isgood(num):
    i, left, right, x = num
    return (
        i and
        hassymbol(grid[i-1][max(0, left-1):min(n, right+1)])
    ) or (
        i < m - 1 and
        hassymbol(grid[i+1][max(0, left-1):min(n, right+1)])
    ) or (
        left and
        hassymbol(grid[i][left-1])
    ) or (
        right < n and
        hassymbol(grid[i][right])
    )


def getval(pi, pj):
    vals = []
    for i, left, right, x in nums:
        if (
            (i == pi - 1 or i == pi + 1) and
            left <= pj + 1 and right >= pj
        ) or (
            i == pi and
            (right == j or left == j + 1)
        ):
            vals.append(x)

    return vals[0] * vals[1] if len(vals) == 2 else 0


tot = 0
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == '*':
            tot += getval(i, j)
print(tot)
