from collections import deque

petrol_pumps = int(input())
stations = deque()

for _ in range(petrol_pumps):
    data = input().split()
    petrol, distance = int(data[0]), int(data[1])
    stations.append({'fuel': petrol, 'distance': distance})

first_station = None
gas_tank = 0

for i in range(petrol_pumps):
    stopped = False
    current_station = i
    while current_station < petrol_pumps:
        gas_tank += stations[current_station]['fuel']
        dist = stations[current_station]['distance']
        if dist > gas_tank:
            stopped = True
            break
        gas_tank -= dist
        current_station += 1
    if gas_tank >= 0 and not stopped:
        first_station = i
        break

print(first_station)