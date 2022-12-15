
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
        if interval_min <= current_max + 1:
            current_max = max(current_max, interval_max)
        else:
            new_intervals.append((current_min, current_max))
            current_min, current_max = interval_min, interval_max
    new_intervals.append((current_min, current_max))


    return new_intervals
length = 4000001
for y in range(0,length):
    if y%1000000==0:
        print(y)

    constraints = []
    for sen in sensors:
        spelrum = manhans[sen] - abs(sen[1]-y)
        if spelrum > 0:
            constraints.append((sen[0]-spelrum, sen[0]+spelrum))

    new_constraints = intervalll_merger(constraints)
    for cons in new_constraints:
        if cons[1] >= 0 and cons[1] <= length-1:
            print("coord:", cons[1]+1, y)
            print(4000000*(cons[1]+1) + y)
            break
