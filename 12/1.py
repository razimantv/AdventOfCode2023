def all_patterns(pattern):
    patterns = [pattern]
    ques = [i for i, c in enumerate(pattern) if c == '?']
    for i in ques:
        newpatterns = []
        for pattern in patterns:
            newpatterns.append(pattern[:i] + '.' + pattern[i+1:])
            newpatterns.append(pattern[:i] + '#' + pattern[i+1:])
        patterns = newpatterns
    return patterns


def runs(pattern):
    ret = [0]
    for c in pattern:
        if c == '#':
            ret[-1] += 1
        elif ret[-1]:
            ret.append(0)

    if not ret[-1]:
        ret.pop()
    return ret


tot = 0
with open('1.2.in') as file:
    for line in file:
        pattern, nums = line[:-1].split(' ')
        nums = [int(x) for x in nums.split(',')]
        tot += len([1 for pat in all_patterns(pattern) if runs(pat) == nums])
        print(tot)
