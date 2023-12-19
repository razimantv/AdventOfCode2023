def previous(ar):
    if max(ar) == min(ar):
        return ar[-1]
    diffs = [ar[i] - ar[i-1] for i in range(1, len(ar))]
    return ar[0] - previous(diffs)


with open('1.2.in') as file:
    tot = sum(
        previous([int(n) for n in line[:-1].split(' ')])
        for line in file
    )
print(tot)
