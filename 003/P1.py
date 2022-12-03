
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","X","Z"]
data = open("In1.txt")
value = 0
for line in data:
    first_half = set()
    second_half = set()
    common = set()
    both = set()
    n = len(line[:-1])
    for i in range(int(n/2)):
        first_half.add(line[i])
    for i in range(int(n/2), n):
        second_half.add(line[i])
    for item in first_half:
        if item in second_half:
            common.add(item)
    print("Common items are ", common)
    for item in common:
        value += alpha.index(item)+1

print(value)