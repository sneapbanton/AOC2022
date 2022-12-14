import os
import time


# Make sure to zoom out in your terminal to see the different partial plots of the solution
# You can increase the wait time between plots at line 79

data = open("In1.txt")
grid = []
width = 1000
for line in data:
    points = line.split("->")
    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i+1]
        x, y = map(int, p1.split(","))
        p1 = (x,y)
        print(p2)
        x, y = map(int, p2.split(","))
        p2 = (x,y)

        if max(p1[1], p2[1]) >= len(grid)-1:
            for j in range(max(p1[1], p2[1]) - len(grid) + 1):
                empty_row = ["." for x in range(width)]
                grid.append(empty_row)
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
            for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
                grid[y][x] = "#"

earliest_x = width
last_x = 0
last_y = 0
counter = 0
s = []
for g in grid:
    counter += 1
    if "#" in g:
        last_y = counter
        if g.index("#") < earliest_x:
            earliest_x = g.index("#")
        g.reverse()
        if len(grid[0]) - g.index("#") - 1 > last_x:
            last_x = len(grid[0]) - g.index("#") - 1
        g.reverse()

def print_board(grid):
    for g in grid[:last_y]:
        row = ""
        for char in g[earliest_x:last_x+1]:
            row += char
        print(row)


def next_pos(grid, current_pos):
    x = current_pos[0]
    y = current_pos[1]
    if y + 1 < last_y and x-1 >= 0 and x+1 < width:
        if grid[y+1][x] == ".":
            return (x, y+1)
        elif grid[y+1][x-1] == ".":
            return (x-1,y+1)
        elif grid[y+1][x+1] == ".":
            return (x+1,y+1)
    return (x,y)


print_board(grid)

fallen_to_bottom = False
starting_pos = (500,0)
last_pos = starting_pos
current_pos = starting_pos
grains_of_sand = 0
while not fallen_to_bottom:
    last_pos = current_pos
    current_pos = next_pos(grid, current_pos)
    if last_pos == current_pos:
        grid[current_pos[1]][current_pos[0]] = "o"
        time.sleep(0.01)
        os.system('cls')
        print_board(grid)
        current_pos = starting_pos
        last_pos = starting_pos
        grains_of_sand += 1
        
    if current_pos[1] >= last_y-1:
        fallen_to_bottom = True


print(grains_of_sand)