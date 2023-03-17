
def recursererserr(data, grid, current_coord, rule, counter, highest_tree):
    new_x = current_coord[0] + rule[0]
    new_y = current_coord[1] + rule[1]
    if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
        return counter - 1
    else:
        if grid[new_y][new_x] >= data:
            return counter
        elif grid[new_y][new_x] < highest_tree:
            return recursererserr(data, grid, (new_x, new_y), rule, counter+1, highest_tree)
        else:
            return recursererserr(data, grid, (new_x,new_y), rule, counter+1, grid[new_y][new_x])

data = open("In1.txt")
grid = []
for line in data:
    row = []
    for height in line:
        if height != '\n':
            row.append(int(height))
    grid.append(row)

factors = []
for y in range(1, len(grid)-1):
    for x in range(1, len(grid[0])-1):
        factor1 = recursererserr(grid[y][x], grid, (x,y), (1,0), 1, 0)
        factor2 = recursererserr(grid[y][x], grid, (x,y), (0,1), 1, 0)
        factor3 = recursererserr(grid[y][x], grid, (x,y), (-1,0), 1, 0)
        factor4 = recursererserr(grid[y][x], grid, (x,y), (0,-1), 1, 0)
        factors.append(factor1*factor2*factor3*factor4)

print(max(factors))