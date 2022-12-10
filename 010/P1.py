
def cycle_check(c):
    if c==20 or c==60 or c==100 or c==140 or c==180 or c==220:
        return True
    return False

data = open("In1.txt")
cycles = 0
x = 1
values = []
last = ""
for line in data:
    if cycle_check(cycles):
        if last == "a":
            values.append((x-n)*cycles)
        else:
            values.append((x)*cycles)
    if line[0] == "n":
        cycles += 1
    else:
        if cycle_check(cycles+1):
            values.append(x*(cycles+1))

        instr, n = line.split(" ")
        n = int(n)
        cycles += 2
        x += n
    last = line[0]

print(sum(values))