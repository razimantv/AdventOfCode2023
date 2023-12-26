process = {}


def accept(x, m, a, s):
    workflow = 'in'
    while workflow not in ['A', 'R']:
        for expr, next in process[workflow][:-1]:
            if eval(expr):
                workflow = next
                break
        else:
            workflow = process[workflow][-1]
    return workflow == 'A'


tot = 0
with open('1.2.in') as file:
    for line in file:
        if len(line) < 2:
            continue
        if line[0] == '{':
            for expr in line[1:-2].split(','):
                exec(expr)
            if accept(x, m, a, s):
                tot += x + m + a + s
        else:
            workflow, rules = line[:-2].split('{')
            process[workflow] = [
                term.split(':') if ':' in term else term
                for term in rules.split(',')
            ]

print(tot)
