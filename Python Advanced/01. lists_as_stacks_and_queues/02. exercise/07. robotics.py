from collections import deque

robots = deque()
abandoned_products = deque()

for robot in input().split(';'):
    robot_name, robot_process_time = robot.split('-')
    robots.append({'name': robot_name, 'process time': int(robot_process_time), 'working time': 0})

starting_hours, starting_minutes, starting_seconds = tuple(map(int, input().split(':')))
hours_to_seconds = starting_hours * 3600
minutes_to_seconds = starting_minutes * 60
total_seconds = hours_to_seconds + minutes_to_seconds + starting_seconds

while True:
    product = input()
    if product == 'End':
        break
    abandoned_products.append(product)

while abandoned_products:
    current_product = abandoned_products[0]
    total_seconds += 1
    for robot in robots:
        if robot['working time'] > 0:
            robot['working time'] -= 1

    for robot in robots:
        if robot['working time'] == 0:
            robot['working time'] = robot['process time']
            h = (total_seconds // 3600) % 24
            m = (total_seconds % 3600) // 60
            s = total_seconds % 60
            print(f"{robot['name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            abandoned_products.popleft()
            break
    else:
        abandoned_products.rotate(-1)
