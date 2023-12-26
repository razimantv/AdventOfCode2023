import random
from collections import defaultdict

full = defaultdict(list)
edges = []
with open('1.2.in') as file:
    i = 0
    for line in file:
        u, vlist = line[:-1].split(': ')
        for v in vlist.split(' '):
            edges.append((i, u, v))
            full[u].append(i)
            full[v].append(i)
            i += 1


def spanning(edges, ignore=None):
    par = {}
    cnt = defaultdict(lambda: 1)
    if ignore is None:
        ignore = []

    def parent(u):
        if u not in par:
            par[u] = u
        elif par[u] != u:
            par[u] = parent(par[u])
        return par[u]

    adj = defaultdict(list)
    edge = []
    for i, u, v in edges:
        if i in ignore:
            edge = (u, v)
            continue
        pu, pv = parent(u), parent(v)
        if pu != pv:
            par[pu] = pv
            cnt[pv] += cnt[pu]
            adj[u].append((i, v))
            adj[v].append((i, u))

    if edge:
        print(cnt[parent(edge[0])] * cnt[parent(edge[1])])
    return adj


def dfs(adj, u, par):
    edges = set(full[u])
    good = set()
    for i, v in adj[u]:
        if v == par:
            continue
        cg, ce = dfs(adj, v, u)
        good = good.union(cg)
        for edge in ce:
            if edge in edges:
                edges.remove(edge)
            else:
                edges.add(edge)
    if len(edges) == 3:
        good = good.union(edges)
    return good, edges


while not (good := dfs(spanning(edges), edges[0][1], -1)[0]):
    random.shuffle(edges)
print([edge for edge in edges if edge[0] in good])
spanning(edges, good)
