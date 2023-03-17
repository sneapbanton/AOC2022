import copy

data = open("In2.txt")

first = False
drawing = []
stacks = dict()
number_of_stacks = 0
for line in data:
    if not first and line[1] != "1":
        drawing.append(line)
    elif not first and len(line) > 1 and line[1] == "1":
        first = True
        for sub in line.split(" "):
            try:
                stacks[int(sub)] = []
                number_of_stacks += 1
            except:
                pass

        for row in drawing:
            for i in range(number_of_stacks):
                if row[4*i+1] != " ":
                    stacks[i+1].append(row[4*i+1])
        for stack in stacks:
            stacks[stack].reverse()

    elif len(line) > 1:
        instruction = line
        filler, n, filler, fro, filler, to = map(str,instruction.split(" "))
        n = int(n)
        fro = int(fro)
        to = int(to)
        moves = copy.copy(stacks[fro][-n:])
        for obj in moves:
            stacks[to].append(obj)
        for i in range(n):
            stacks[fro].pop(-1)

out_string = ""
for stack in stacks:
    if len(stacks[stack]):
        out_string += stacks[stack][-1]
print(out_string)