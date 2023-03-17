
import json

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
indexes = []
for i in range(int(len(lines)/2)):
    l1 = lines[2*i]
    l2 = lines[(2*i)+1]
    correct = matcherer(l1, l2)
    if correct == 1:
        indexes.append(i+1)


print(sum(indexes))

