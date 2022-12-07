
total_sizes_under_100 = 0
dirs = []
def recurrerreresrr():
    global total_sizes_under_100
    global dirs
    size_files = 0
    size_sub_dirs = 0
    while len(commands):
        command = commands.pop(0)
        if command[:4] == "$ ls":
            ls = []
            while len(commands):
                if commands[0][0] != "$":
                    ls.append(commands[0])
                    commands.pop(0)
                else:
                    break
            for row in ls:
                info, name = row.split(" ")
                if info != "dir":
                    size_files += int(info) #add size of file

        elif command[:4] == "$ cd" and command[:7] != "$ cd ..":
            sub_size = recurrerreresrr()
            dirs.append(sub_size)
            if sub_size <= 100000:
                size_sub_dirs += sub_size
            else:
                size_files += sub_size


        elif command[:7] == "$ cd ..":
            #print("size of size_files ", size_files)
            #print("size of size_sub_dirs ", size_sub_dirs)
            #if size_files + size_sub_dirs > 100000:
            #    print("EHRER:::::_______----")
            #    total_sizes_under_100 += size_sub_dirs
            break
    if size_files + size_sub_dirs <= 100000:
        total_sizes_under_100 += size_files + size_sub_dirs
    return size_files + size_sub_dirs

data = open("In1.txt")
commands = []
for line in data:
    commands.append(line)

first_command = commands.pop(0)
amount = recurrerreresrr()
dirs.append(amount)
dirs.sort()
for dir in dirs:
    if 70000000 - amount + dir >= 30000000:
        break
print(dir)
