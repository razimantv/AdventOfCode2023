from collections import defaultdict

colors = ['red', 'green', 'blue']
tot = 0
with open('1.2.in') as file:
    for id, line in enumerate(file):
        maxcnt = defaultdict(int)
        line = line[:-1].split(':')[1]
        for attempt in line.split(';'):
            for colour in attempt.split(','):
                cnt, clr = colour[1:].split(' ')
                maxcnt[clr] = max(maxcnt[clr], int(cnt))

        cur = 1
        for clr in colors:
            cur *= maxcnt[clr]
        tot += cur

print(tot)
