from collections import deque

petrol_pumps = int(input())
stations = deque()

for _ in range(petrol_pumps):
    data = input().split()
    petrol, distance = int(data[0]), int(data[1])
    stations.append({'fuel': petrol, 'distance': distance})

changes = 0

while changes < petrol_pumps:
    gas_tank = 0
    for i in range(petrol_pumps):
        gas_tank += stations[i]['fuel']
        dist = stations[i]['distance']
        if dist > gas_tank:
            changes += 1
            stations.rotate(-1)
            gas_tank -= dist
            break
        gas_tank -= dist
    if gas_tank >= 0:
        first_station = changes
        break

print(changes)