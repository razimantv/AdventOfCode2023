from collections import defaultdict
pref, psum = defaultdict(int), 0

tot = 0
with open('1.2.in') as file:
    for i, line in enumerate(file):
        psum += pref[i]
        tot += psum + 1
        data = line.split(':')[1].split('|')
        good = [
            set(int(x) for x in dat[1:-1].split(' ') if x)
            for dat in data
        ]
        intersection = len(good[0].intersection(good[1]))
        pref[i + 1] += psum + 1
        pref[i + 1 + intersection] -= psum + 1
print(tot)
