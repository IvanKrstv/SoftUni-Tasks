fire_cells = input().split("#")
water = int(input())

total_effort = 0
cells = []
for element in fire_cells:
    new_element = element.split(" = ")
    fire_type = new_element[0]
    value_cell = int(new_element[1])
    if water <= 0:
        break
    if value_cell > water:
        continue
    if fire_type == "High" and 81 <= value_cell <= 125:
        pass
    elif fire_type == "Medium" and 51 <= value_cell <= 80:
        pass
    elif fire_type == "Low" and 1 <= value_cell <= 50:
        pass
    else:
        continue
    water -= value_cell
    cells.append(value_cell)
    total_effort += value_cell * 0.25

print("Cells:")
for i in range(len(cells)):
    print(f" - {cells[i]}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(cells)}")