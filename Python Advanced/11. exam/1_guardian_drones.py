from collections import deque

mechanical_parts = [int(x) for x in input().split()]
power_cells = deque(int(x) for x in input().split())

models = {
    100: 'Sentinel-X',
    85: 'Viper-MKII',
    75: 'Aegis-7',
    65: 'Striker-R',
    55: 'Titan-Core'
}
built_models = []

while mechanical_parts and power_cells and len(built_models) < 5:
    current_part = mechanical_parts.pop()
    current_cell = power_cells.popleft()
    while current_cell <= 0:
        current_cell = power_cells.popleft()

    total_activation_power = current_part + current_cell
    if total_activation_power in models.keys() and models[total_activation_power] not in built_models:
        built_models.append(models[total_activation_power])
    else:
        for pwr, drone in models.items():
            if pwr < total_activation_power and drone not in built_models:
                built_models.append(drone)
                new_cell =current_cell - 30
                if new_cell > 0:
                    power_cells.append(new_cell)
                break
        else:
            new_cell = current_cell - 1
            if new_cell > 0:
                power_cells.append(new_cell)

if len(built_models) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")
if built_models:
    print(f"Assembled Drones: {', '.join(str(x) for x in built_models)}")
if mechanical_parts:
    print(f"Mechanical Parts: {', '.join(str(x) for x in reversed(mechanical_parts))}")
if power_cells and not all(x == 0 for x in power_cells):
    print(f"Power Cells: {', '.join(str(x) for x in power_cells if x != 0)}")