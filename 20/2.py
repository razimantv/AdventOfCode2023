from collections import defaultdict
import queue

graph = defaultdict(lambda: ['', []])
rev = defaultdict(dict)

with open('1.3.in') as file:
    for line in file:
        src, dests = line[:-1].split(' -> ')
        dests = dests.split(', ')
        if src[0] == 'b':
            kind = 'b'
        else:
            src, kind = src[1:], src[0]
        graph[src] = [kind, dests]
        if kind == '%':
            graph[src].append('off')
        for dest in dests:
            rev[dest][src] = 'low'

bfsq = queue.Queue()

print([u for u in rev['ll']])
for i in range(10000):
    bfsq.put(('button', 'broadcaster', 'low'))
    while not bfsq.empty():
        src, dest, pulse = bfsq.get()
        if src in rev['ll'] and pulse == 'high':
            print(f'{i + 1}: {src} -{pulse}-> {dest}')
        node = graph[dest]
        rev[dest][src] = pulse
        match node[0]:
            case 'b':
                nextpulse = pulse
            case '%':
                if pulse == 'high':
                    continue
                node[-1], nextpulse = (
                    ('on', 'high') if node[-1] == 'off' else ('off', 'low')
                )
            case '&':
                nextpulse = 'high' if 'low' in rev[dest].values() else 'low'
        for next in node[1]:
            bfsq.put((dest, next, nextpulse))
    else:
        continue
    break
