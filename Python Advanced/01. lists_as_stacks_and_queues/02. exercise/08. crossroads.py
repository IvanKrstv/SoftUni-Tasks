from collections import deque

cars = deque()
passed_car = 0

duration_green_light = int(input())
duration_free_window = int(input())

while True:
    command = input()
    if command == 'END':
        print(f"Everyone is safe."
              f"\n{passed_car} total cars passed the crossroads.")
        break

    elif command == 'green':
        green_light_cycle = duration_green_light
        while cars and green_light_cycle > 0:
            car = cars.popleft()
            car_length = len(car)

            if car_length <= green_light_cycle:
                green_light_cycle -= car_length
                passed_car += 1
            elif car_length <= green_light_cycle + duration_free_window:
                green_light_cycle = 0
                passed_car += 1
            else:
                crash_point = green_light_cycle + duration_free_window
                print(f"A crash happened!"
                      f"\n{car} was hit at {car[crash_point]}.")
                exit()
    else:
        cars.append(command)
