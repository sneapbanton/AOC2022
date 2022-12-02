
data = open("In2.txt")
rules = {"A Y":3, "A X":0, "A Z": 6, "B X": 0, 
        "B Y": 3, "B Z":6, "C X": 0, "C Y":3, "C Z":6}
win = {"A":"B", "B":"C", "C":"A"}
lose = {"B":"A", "C":"B", "A":"C"}
shape = {"A":1, "B":2, "C":3}

points = 0
for line in data:
    if line[2] == "X":
        action = lose[line[0]]
    elif line[2] == "Y":
        action = line[0]
    elif line[2] == "Z":
        action = win[line[0]]

    points += rules[line[:3]] + shape[action]

print(points)