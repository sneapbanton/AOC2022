

def get_possible_neighs(coord):
    possible_neighs = []
    current_height = grid[coord[1]][coord[0]]
    if coord[1] < len(grid) - 1:
        if abs(current_height - grid[coord[1] + 1][coord[0]]) <= 1:
            possible_neighs.append((coord[0], coord[1] + 1, "^"))
    if coord[1] > 0:
        if abs(current_height - grid[coord[1] - 1][coord[0]]) <= 1:
            possible_neighs.append((coord[0], coord[1] - 1, "V"))   
    if coord[0] > 0:
        if abs(current_height - grid[coord[1]][coord[0] - 1]) <= 1:
            possible_neighs.append((coord[0] - 1, coord[1], ">")) 
    if coord[0] < len(grid[0]) - 1:
        if abs(current_height - grid[coord[1]][coord[0] + 1]) <= 1:
            possible_neighs.append((coord[0] + 1, coord[1], "<")) 
    return possible_neighs

data = open("test1.txt")
grid = []
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']

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

print(grid)
visited = [['.' for i in range(len(grid[0]))] for x in range(len(grid))]
print(visited)

queue = [(start_x, start_y)]
while queue:
    current_elem = queue.pop(0)
    if current_elem[0] == end_x and current_elem[1] == end_y:
        break
    neighs = get_possible_neighs(current_elem)
    for neigh in neighs:
        print(neigh[1], " ", neigh[0])
        if visited[neigh[1]][neigh[0]] == ".":
            visited[neigh[1]][neigh[0]] = neigh[2]
            queue.append(neigh)

for r in visited:
    print(r)
