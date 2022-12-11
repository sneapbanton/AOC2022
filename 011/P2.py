from collections import defaultdict

def alter(modifier, current, value):
    if value == "old":
        value = current
    value = int(value)
    if modifier == "+":
        return current + value
    else:
        return current * value


data = open("In1.txt")

monkey = defaultdict(list)
operations = []
modifiers = []
dividers = []
true_monke = []
false_monke = []
inspected = [0] * 10
current_monke = 0
the_great_divider = 1
for line in data:

    if line[:6] == "Monkey":
        current_monke = int(line[7])
    elif line[2:7] == "Start":
        values = line[17:].split(" ")
        for v in values[1:]:
            if v[-1] == ",":
                v = v[:-1]
            monkey[current_monke].append(int(v))

    elif line[2:7] == "Opera":
        oper = line[23]
        operations.append(oper)
        modifiers.append(line[25:-1])

    elif line[2:6] == "Test":
        divider = int(line[2:].split(" ")[3])
        dividers.append(int(divider))
        the_great_divider = the_great_divider * int(divider)

    elif line[4:8] == "If t":
        to_monke = int(line[4:].split(" ")[-1])
        true_monke.append(int(to_monke))

    elif line[4:8] == "If f":
        to_monke = int(line[4:].split(" ")[-1])
        false_monke.append(int(to_monke))

for i in range(10000):
    for monke in range(len(operations)):
        for j in range(len(monkey[monke])):
            inspected[monke] += 1
            item = monkey[monke].pop(0)
            item = int(alter(operations[monke], item, modifiers[monke])) % the_great_divider
            if item % dividers[monke] == 0:
                monkey[true_monke[monke]].append(item)
            else:
                monkey[false_monke[monke]].append(item)

inspected.sort(reverse=True)
print(inspected)
print(inspected[0], " ", inspected[1])
print(inspected[0]*inspected[1])