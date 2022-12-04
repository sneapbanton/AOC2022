

data = open("In1.txt")
counter = 0
for line in data:
    first, second = map(str, line.split(","))
    if second[-1]=='\n':
        second = second[:-1]

    first_set = set()
    second_set = set()
    a,b = map(int, first.split("-"))
    for i in range(a, b+1):
        first_set.add(i)
    a,b = map(int, second.split("-"))
    for i in range(a, b+1):
        second_set.add(i)
    if first_set.issubset(second_set) or second_set.issubset(first_set):
        counter += 1
print(counter)