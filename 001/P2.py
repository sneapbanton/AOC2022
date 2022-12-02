
elfs = []
data = open("In1.txt")
prev = "\n"
for line in data:
    if prev == "\n" and line != "\n":
        elfs.append(int(line))
    elif line != "\n":
        elfs[-1] = elfs[-1] + int(line)
    prev = line

elfs.sort()
elfs.reverse()

print(elfs[0]+elfs[1]+elfs[2])