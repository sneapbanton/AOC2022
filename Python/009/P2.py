import numpy as np

def walk_rule(dir):
    if dir == "U":
        return (0,1)
    elif dir == "D":
        return (0,-1)
    elif dir == "L":
        return (-1,0)
    elif dir == "R":
        return (1,0)
    return 0

data = open("In1.txt")
hx = 0
hy = 0
tx = 0
ty = 0
visited = set()
tail = [(0,0) for x in range(10)]
for line in data:
    direction, n = line.split(" ")
    rule_for_walk = walk_rule(direction)
    n = int(n)
    for i in range(n):
        hx = hx + rule_for_walk[0]
        hy = hy + rule_for_walk[1]
        
        new_tail = [(0,0) for x in range(10)]
        new_tail[0] = (hx, hy)

        for t in range(len(tail)-1):
            t1 = new_tail[t]
            t2 = tail[t+1]
            if abs(t1[0]-t2[0]) <= 1 and abs(t1[1]-t2[1]) <= 1:
                new_tail[t+1] = tail[t+1]
            else:
                x_mod = np.sign(t1[0]-t2[0])
                y_mod = np.sign(t1[1]-t2[1])
                new_tail[t+1] = (tail[t+1][0] + x_mod, tail[t+1][1] + y_mod)
            
        for t in range(len(tail)):
            tail[t] = new_tail[t]

        visited.add(tail[9])

visited.add(tail[9])

print(len(visited))