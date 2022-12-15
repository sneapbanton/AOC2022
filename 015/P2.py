
data = open("In1.txt")



manhans = dict()
sensors = []
beacons = set()

for line in data:
    sensorx = int(line[line.index("x=")+2:].split(" ")[0][:-1])
    sensory = int(line[line.index("y=")+2:].split(" ")[0][:-1])
    beaconx = int(line[line.index(":"):][line[line.index(":"):].index("x="):][2:].split(" ")[0][:-1])
    if line[-1:] == '\n':
        beacony = int(line[line.index(":"):][line[line.index(":"):].index("y="):][2:].split(" ")[0][:-1])
    else:
        beacony = int(line[line.index(":"):][line[line.index(":"):].index("y="):][2:].split(" ")[0])

    manhans[(sensorx, sensory)] = abs(sensorx-beaconx) + abs(sensory-beacony)
    sensors.append((sensorx, sensory))
    beacons.add((beaconx, beacony))

coord = (-1,-1)
for y in range(0, 4000000):
    if y%1000000 == 0:
        print("y", y)
    for x in range(0, 4000000):
        if x%1000000 == 0:
            print("x", x)
        cond = True
        for sen in sensors:
            if abs(sen[0]-x) + abs(sen[1]-y) <= manhans[sen]:
                cond = False
                break
        if cond:
            print("coord is ", x, y)
            coord = (x, y)
            break

print(coord)