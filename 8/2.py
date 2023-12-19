moves = 'LRRRLLRLLRRLRLRRRLRLRRRLRRLLRRRLRRLRLLRLLRRLRLLLLRRLRRLRLLRRLRRRLLLRRLRLRRLRRRLRRRLLRLRRRLLRRLRRRLRRLRLRRLRRLLRLRLRRRLRRLRRLRRRLRRLRRLRLRRRLRRRLRRRLLLRLRRLRLRRRLRRRLRRLRRLLRLRRLLRRLLRLRRLRLRRLRRRLRLRRLRLRRRLLRRLLRLRRRLRRRLRRRLRRRLLLRLRRLRRRLRRRLRLLRRLLRRLRLRLLRRLRRLLRRRLRLRRRLRRRR'
next = {}
with open('1.2.in') as file:
    for line in file:
        cur, left, right = line[:-1].split(' ')
        next[cur] = (left, right)


for pos in filter(lambda x: x[-1] == 'A', next):
    n, i, tot = len(moves), 0, 0
    print(pos)
    for round in range(2):
        while True:
            pos = next[pos][1 if moves[i] == 'R' else 0]
            i = (i + 1) % n
            tot += 1
            if pos[-1] == 'Z':
                break
        print(tot)
