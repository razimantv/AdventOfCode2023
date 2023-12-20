process = {}
cmap = {'x': 0, 'm': 1, 'a': 2, 's': 3}


def volume(cuboid):
    ret = 1
    for l, r in cuboid:
        ret *= (r - l + 1)
    return ret


def goodvolume(workflow, cuboid):
    if workflow == 'R':
        return 0
    elif workflow == 'A':
        return volume(cuboid)

    ret = 0
    cuboids = [cuboid]
    for var, (l, r), next in process[workflow][:-1]:
        nextcuboids = []
        for cuboid in cuboids:
            l0, r0 = cuboid[var]
            if r0 < l or l0 > r:
                nextcuboids.append(cuboid)
                continue
            ret += goodvolume(
                next,
                cuboid[:var] + [(max(l, l0), min(r, r0))] + cuboid[var+1:]
            )
            if l0 < l:
                nextcuboids.append(
                    cuboid[:var] + [(l0, l-1)] + cuboid[var+1:]
                )
            if r0 > r:
                nextcuboids.append(
                    cuboid[:var] + [(r+1, r0)] + cuboid[var+1:]
                )
        cuboids = nextcuboids

    return ret + sum(
        goodvolume(process[workflow][-1], cuboid)
        for cuboid in cuboids
    )


with open('1.2.in') as file:
    for line in file:
        if len(line) < 2 or line[0] == '{':
            continue
        workflow, rules = line[:-2].split('{')
        ruleranges = []
        for term in rules.split(','):
            if ':' not in term:
                ruleranges.append(term)
                break
            term, target = term.split(':')
            var = cmap[term[0]]
            vlim = int(term[2:])
            vrange = (1, vlim-1) if term[1] == '<' else (vlim+1, 4000)
            ruleranges.append([var, vrange, target])
        process[workflow] = ruleranges

print(goodvolume('in', [(1, 4000)] * 4))
