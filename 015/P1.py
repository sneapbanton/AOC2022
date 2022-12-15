
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


def intervalll_merger(intervals):
    intervals.sort(key=lambda interval: interval[0])

    # merge the intervals
    new_intervals = []
    current_min, current_max = intervals[0]
    for interval_min, interval_max in intervals:
        if interval_min <= current_max:
            current_max = max(current_max, interval_max)
        else:
            new_intervals.append((current_min, current_max))
            current_min, current_max = interval_min, interval_max
    new_intervals.append((current_min, current_max))


    return new_intervals


counter = 0
y = 2000000
length = 4000000

constraints = []
for sen in sensors:
    spelrum = manhans[sen] - abs(sen[1]-y)
    if spelrum > 0:
        constraints.append((sen[0]-spelrum, sen[0]+spelrum))

new_constraints = intervalll_merger(constraints)

counter = 0
for cons in new_constraints:
    counter += len(range(cons[0], cons[1]+1))

beac_counter = 0
for beacon in beacons:
    if beacon[1] == y:
        beac_counter += 1

print(counter-beac_counter)