
data = open("In1.txt")
rules = {"A Y":6, "A X":3, "A Z": 0, "B X": 0, 
        "B Y": 3, "B Z":6, "C X": 6, "C Y":0, "C Z":3}
shape = {"X":1, "Y":2, "Z":3}

points = 0
for line in data:
    points += rules[line[:3]] + shape[line[2]]

print(points)