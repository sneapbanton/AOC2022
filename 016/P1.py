import copy
from collections import defaultdict

data = open("test1.txt")
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

def highest_flow(opened):
    summer = 0
    for o in opened:
        summer += flows[(o[0])]*int(o[1])
    return summer
    

def remove_overlap(valves):
    opened = set()
    new_valves = []
    valves.sort(key=lambda x:x[1], reverse=True)
    for v in valves:
        if v[0] not in opened:
            new_valves.append(v)
            opened.add(v[0])
    return new_valves


dp = [defaultdict(list) for x in range(31)]


def traverserrr(minutes_left, current, open):
    global dp
    if minutes_left <= 0:
        dp[0][current] = []
        return

    coolest_list = []
    if open:
        print("open is ", open)

    neigh_tunnels = tunnels[current]
    for neigh in neigh_tunnels:
        if minutes_left - 2 >= 0 and flows[current]:
            new_open = copy.deepcopy(open)
            new_open.append((current, minutes_left-1))

            if not len(dp[minutes_left-2][neigh]):
                traverserrr(minutes_left-2, neigh, new_open)

            
            cool_list = copy.deepcopy(dp[minutes_left-2][current])
            cool_list.extend(new_open)
            even_cooler_list = remove_overlap(cool_list)

            if highest_flow(even_cooler_list) > highest_flow(coolest_list):
                coolest_list = even_cooler_list

        if not len(dp[minutes_left-1][neigh]):
            traverserrr(minutes_left-1, neigh, open)

        cool_list = copy.deepcopy(dp[minutes_left-2][current])
        cool_list.extend(open)
        even_cooler_list = remove_overlap(cool_list)

        if highest_flow(even_cooler_list) > highest_flow(coolest_list):
            coolest_list = even_cooler_list    

    dp[minutes_left][current] = coolest_list
        

traverserrr(30, "AA", [])
print(highest_flow(dp[30]))
print(dp[30])


