
def cycle_check(c):
    if c==40 or c==80 or c==120 or c==160 or c==200 or c==240:
        return True
    return False


def drawer(sprite_pos, cycle):
    cycle = cycle%40
    if abs(sprite_pos - cycle) <= 1:
        return "#"
    else:
        return "."

data = open("In1.txt")
cycles = 0
x = 1
screen = []
row = ""
for line in data:
    if cycle_check(cycles):
        screen.append(row)
        row = ""

    row += drawer(x, cycles)

    if line[0] == "n":
        cycles += 1

    else:
        cycles += 1
        if cycle_check(cycles):
            screen.append(row)
            row = ""

        row += drawer(x, cycles)

        instr, n = line.split(" ")
        n = int(n)
        cycles += 1
        x += n
screen.append(row)
for r in screen:
    print(r)