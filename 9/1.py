def next(ar):
    if max(ar) == min(ar):
        return ar[-1]
    diffs = [ar[i] - ar[i-1] for i in range(1, len(ar))]
    return next(diffs) + ar[-1]


with open('1.2.in') as file:
    tot = sum(
        next([int(n) for n in line[:-1].split(' ')])
        for line in file
    )
print(tot)
