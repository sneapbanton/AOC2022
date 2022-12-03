from collections import defaultdict
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","X","Z"]
data = open("In1.txt")
final_value = 0
elfs = 0
common = defaultdict(int)
for line in data:
    if elfs % 3 == 0 and elfs != 0:
        for key,value in common.items():
            if value == 3:
                final_value += alpha.index(key)+1
                print("Value for ", key, " is ", alpha.index(key)+1)
                print("for elf ", elfs, " common are ", key)

        common = defaultdict(int)

    first_half = set()
    second_half = set()
    n = len(line[:-1])
    for i in range(int(n/2)):
        first_half.add(line[i])
    for i in range(int(n/2), n):
        second_half.add(line[i])
    for item in first_half:
        common[item] += 1
    for item in second_half:
        common[item] += 1
    elfs += 1
    
for key,value in common.items():
    if value == 3:
        final_value += alpha.index(key)+1
        print("Value for ", key, " is ", alpha.index(key)+1)
        print("for elf ", elfs, " common are ", key)
print(final_value)