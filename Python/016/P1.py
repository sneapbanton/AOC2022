import copy
from collections import defaultdict

data = open("test1.txt")
flows = dict()
tunnels = dict()
dists = defaultdict(dict)
for line in data:
    words = line.split(" ")
    name = words[1]
    flowrate = int(words[4][5:-1])
    leads_to = words[9:]
    for i in range(len(leads_to)):
        if leads_to[i][-1] in [',', '\n']:
            leads_to[i] = leads_to[i][:-1]
    flows[name] = flowrate
    tunnels[name] = leads_to

def highest_flow(opened):
    summer = 0
    for o in opened:
        summer += flows[(o[0])]*int(o[1])
    return summer

def bfs(start):
    visited = []
    queue = [(start, 0)]
    while queue:
        current, depth = queue.pop(0)
        visited.append(current)
        if current != start and flows[current]:
            dists[start][current] = depth
        for neigh in tunnels[current]:
            if neigh not in visited:
                queue.append((neigh, depth+1)) # type: ignore




