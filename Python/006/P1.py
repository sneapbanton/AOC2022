

data = open("In1.txt")
for line in data:
    line = line[:-1]
    matching = [line[0],line[1],line[2]]
    for i in range(3, len(line)):
        if len(matching) == 4:
            matching.pop(0)
        new_char = line[i]
        matching.append(new_char)
        if len(set(matching)) == 4:
            print(i+1)
            break