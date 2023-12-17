tot = 0
with open('1.2.in') as file:
    for line in file:
        digs = [c for c in line if c.isdigit()]
        tot += int(digs[0] + digs[-1])

print(tot)
