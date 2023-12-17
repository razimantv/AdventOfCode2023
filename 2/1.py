maxcnt = {'red': 12, 'green': 13, 'blue': 14}

tot = 0
with open('1.2.in') as file:
    for id, line in enumerate(file):
        line = line[:-1].split(':')[1]
        for attempt in line.split(';'):
            for colour in attempt.split(','):
                cnt, clr = colour[1:].split(' ')
                if clr not in maxcnt or maxcnt[clr] < int(cnt):
                    break
            else:
                continue
            break
        else:
            tot += id + 1

print(tot)
