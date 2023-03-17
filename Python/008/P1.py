

def recursererserr(data, grid, current_coord, rule):
    new_x = current_coord[0] + rule[0]
    new_y = current_coord[1] + rule[1]
    if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
        return True
    elif grid[new_y][new_x] >= data:
        return False
    return recursererserr(data, grid, (new_x,new_y), rule)

data = open("In1.txt")
grid = []
for line in data:
    row = []
    for height in line:
        if height != '\n':
            row.append(int(height))
    grid.append(row)

counter = 2*len(grid) + 2*len(grid[0]) - 4

for y in range(1, len(grid)-1):
    for x in range(1, len(grid[0])-1):

        if recursererserr(grid[y][x], grid, (x,y), (1,0)):
            counter += 1

        elif recursererserr(grid[y][x], grid, (x,y), (0,1)):
            counter += 1

        elif recursererserr(grid[y][x], grid, (x,y), (-1,0)):
            counter += 1

        elif recursererserr(grid[y][x], grid, (x,y), (0,-1)):
            counter += 1


print(counter)