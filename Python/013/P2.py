
import json
import copy

def matcherer(left, right):
    #print("left is ", left)
    #print("right is ", right)
    #print()
    if len(left) and not len(right):
        return -1
    if not len(left) and len(right):
        return 1
    if not len(left) and not len(right):
        return 0

    if isinstance(left[0], int) and isinstance(right[0], int):
        if left[0] < right[0]:
            return 1
        elif left[0] == right[0]:
            return matcherer(left[1:], right[1:])
        else:
            return -1

    elif isinstance(left[0], list) and isinstance(right[0], int):
        answer = matcherer(left[0], [right[0]])
        if answer == 0:
            return matcherer(left[1:], right[1:])
        else:
            return answer

    elif isinstance(left[0], int) and isinstance(right[0], list):
        answer = matcherer([left[0]], right[0])
        if answer == 0:
            return matcherer(left[1:], right[1:])
        else:
            return answer

    elif isinstance(left[0], list) and isinstance(right[0], list):
        answer = matcherer(left[0], right[0])
        if answer == 0:
            return matcherer(left[1:], right[1:])
        else:
            return answer
    

data = open("In1.txt")
lines = []
for line in data:
    if line != "\n":
        res = json.loads(line)
        lines.append(res)

lines.append([[2]])
lines.append([[6]])    
changed = True
while changed:
    changed = False
    for i in range(int(len(lines))-1):
        l1 = lines[i]
        l2 = lines[i+1]
        correct = matcherer(l1, l2)
        if correct == -1:
            changed = True
            copy_l1 = copy.deepcopy(l1)
            lines[i] = l2
            lines[i+1] = copy_l1

print((lines.index([[2]])+1) * (lines.index([[6]])+1))

