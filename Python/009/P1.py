
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

for line in data:
    direction, n = line.split(" ")
    rule_for_walk = walk_rule(direction)
    n = int(n)
    for i in range(n):
        new_hx = hx + rule_for_walk[0]
        new_hy = hy + rule_for_walk[1]
        if abs(new_hx-tx) <= 1 and abs(new_hy-ty) <= 1:
            pass
        else:
            visited.add((tx,ty))
            tx = hx
            ty = hy
            
        hx = new_hx
        hy = new_hy
visited.add((tx,ty))

print(len(visited))