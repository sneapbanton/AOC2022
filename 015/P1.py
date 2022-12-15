
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

counter = 0
y = 2000000
for x in range(-1000000, 5000000):
    if x%1000001 == 0:
        print(x)
    for sen in sensors:
        if abs(sen[0]-x) + abs(sen[1]-y) <= manhans[sen]:
            counter += 1
            break

for beacon in beacons:
    if beacon[1] == y:
        counter -= 1

print(counter)