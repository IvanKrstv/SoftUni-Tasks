size_field = int(input())

field = []
bunny_pos = (0, 0)

for i in range(size_field):
    row = input().split()
    field.append(row)
    for j in range(size_field):
        if field[i][j] == 'B':
            bunny_pos = (i, j)

possible_moves = {'down': (1, 0), 'up': (-1, 0), 'left': (0, -1), 'right': (0, 1)}
max_eggs_side = ''
max_eggs = float('-inf')
max_coords = []

for move, coords in possible_moves.items():
    current_row, current_col = bunny_pos[0] + coords[0], bunny_pos[1] + coords[1]
    current_eggs = 0
    current_coords = []

    while 0 <= current_row < size_field and 0 <= current_col < size_field:
        if field[current_row][current_col] == 'X':
            break

        current_eggs += int(field[current_row][current_col])
        current_coords.append([current_row, current_col])

        current_row += coords[0]
        current_col += coords[1]

    if current_eggs > max_eggs and current_coords:
        max_eggs = current_eggs
        max_eggs_side = move
        max_coords = current_coords

print(max_eggs_side)
for cord in max_coords:
    print(cord)
print(max_eggs)

