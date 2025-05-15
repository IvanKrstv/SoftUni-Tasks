n = int(input())
cars_set = set()

for _ in range(n):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        cars_set.add(car_number)
    elif direction == 'OUT':
        cars_set.remove(car_number)

if not cars_set:
    print("Parking Lot is Empty")
else:
    print('\n'.join(cars_set))
