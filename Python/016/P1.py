
data = open("In1.txt")
flows = dict()
tunnels = dict()
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

from collections import defaultdict
from functools import cache

visited = defaultdict(lambda: -1)

@cache
def dfs(curr, flow, opened, time):

    if visited[curr+str(flow)] != -1 and visited[curr+str(flow)] >= time:
        return 0
    if time==0:
        return flow
    vals = []
    for neigh in tunnels[curr]:
        if neigh not in opened and flows[neigh] and time > 2:
            new_flow = flow + flows[neigh]*(time-2)
            new_opened = list(opened)
            new_opened.append(neigh)
            vals.append(dfs(neigh, new_flow, tuple(new_opened), time-2))
        vals.append(dfs(neigh, flow, opened, time-1))
    visited[curr+str(flow)] = time
    return max(vals)


print(dfs("AA", 0, tuple([]), 30))
