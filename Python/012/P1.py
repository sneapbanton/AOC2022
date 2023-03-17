

def get_possible_neighs(coord):
    possible_neighs = []
    current_height = grid[coord[1]][coord[0]]
    if coord[1] < len(grid) - 1:
        if grid[coord[1] + 1][coord[0]] < current_height or abs(current_height - grid[coord[1] + 1][coord[0]]) <= 1:
            possible_neighs.append((coord[0], coord[1] + 1, "^"))
    if coord[1] > 0:
        if grid[coord[1] - 1][coord[0]] < current_height or abs(current_height - grid[coord[1] - 1][coord[0]]) <= 1:
            possible_neighs.append((coord[0], coord[1] - 1, "V"))   
    if coord[0] > 0:
        if grid[coord[1]][coord[0] - 1] < current_height or abs(current_height - grid[coord[1]][coord[0] - 1]) <= 1:
            possible_neighs.append((coord[0] - 1, coord[1], ">")) 
    if coord[0] < len(grid[0]) - 1:
        if grid[coord[1]][coord[0] + 1] < current_height or abs(current_height - grid[coord[1]][coord[0] + 1]) <= 1:
            possible_neighs.append((coord[0] + 1, coord[1], "<")) 
    return possible_neighs

data = open("In1.txt")
grid = []
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

start_x = 0
start_y = 0
end_x = 0
end_y = 0

for line in data:
    row = []
    for char in line:
        if char == 'S':
            start_x = line.index(char)
            start_y = len(grid)
            row.append(0)
        elif char == 'E':
            end_x = line.index(char)
            end_y = len(grid)
            row.append(25)
        elif char and char != '\n':
            row.append(alpha.index(char))
    grid.append(row)

print(start_x, " ", start_y)
print(end_x, " ", end_y)
visited = [['.' for i in range(len(grid[0]))] for x in range(len(grid))]

"""
queue = [(end_x, end_y)]
while queue:
    current_elem = queue.pop(0)
    if current_elem[0] == start_x and current_elem[1] == start_y:
        break
    neighs = get_possible_neighs(current_elem)
    for neigh in neighs:
        if (neigh[0], neigh[1]) != (end_x, end_y) and visited[neigh[1]][neigh[0]] == ".":
            visited[neigh[1]][neigh[0]] = neigh[2]
            queue.append(neigh)

for r in visited:
    print(r)

def upnestler(coord):
    print("coord is ", coord)
    arrow = visited[coord[1]][coord[0]]
    if arrow == "^":
        return (coord[0], coord[1]-1)
    elif arrow == "V":
        return (coord[0], coord[1]+1)
    elif arrow == "<":
        return (coord[0]-1, coord[1])
    elif arrow == ">":
        return (coord[0]+1, coord[1])

current_coord = (start_x, start_y)
counter = 0
while current_coord != (end_x, end_y):
    current_coord = upnestler(current_coord)
    counter += 1
print(counter)



"""
queue = [(start_x, start_y)]
while queue:
    current_elem = queue.pop(0)
    if current_elem[0] == end_x and current_elem[1] == end_y:
        break
    neighs = get_possible_neighs(current_elem)
    for neigh in neighs:
        if (neigh[0], neigh[1]) != (start_x, start_y) and visited[neigh[1]][neigh[0]] == ".":
            visited[neigh[1]][neigh[0]] = neigh[2]
            queue.append(neigh)

for r in visited:
    row = ""
    for char in r:
        row += char
    print(row)

def upnestler(coord):
    arrow = visited[coord[1]][coord[0]]
    if arrow == "^":
        return (coord[0], coord[1]-1)
    elif arrow == "V":
        return (coord[0], coord[1]+1)
    elif arrow == "<":
        return (coord[0]-1, coord[1])
    elif arrow == ">":
        return (coord[0]+1, coord[1])

current_coord = (end_x, end_y)
counter = 0
while current_coord != (start_x, start_y):
    current_coord = upnestler(current_coord)
    counter += 1
print(counter)
