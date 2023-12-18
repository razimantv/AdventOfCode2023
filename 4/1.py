tot = 0
with open('1.2.in') as file:
    for line in file:
        data = line.split(':')[1].split('|')
        good = [
            set(int(x) for x in dat[1:-1].split(' ') if x)
            for dat in data
        ]
        intersection = good[0].intersection(good[1])
        tot += (1 << (len(intersection) - 1)) if intersection else 0
print(tot)
