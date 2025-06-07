n = int(input())
matrix = [list(input()) for _ in range(n)]
pos_bee = (0, 0)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'B':
            pos_bee = (i, j)

energy = 15
is_restored = False
collected_nectar = 0
NECTAR_FOR_HONEY = 30

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()
    current_row, current_col = pos_bee
    matrix[current_row][current_col] = '-'

    current_row += moves[command][0]
    current_col += moves[command][1]
    if current_row >= n:
        current_row = 0
    if current_row < 0:
        current_row = n - 1
    if current_col >= n:
        current_col = 0
    if current_col < 0:
        current_col = n - 1

    new_place = matrix[current_row][current_col]
    energy -= 1
    pos_bee = (current_row, current_col)
    matrix[pos_bee[0]][pos_bee[1]] = 'B'

    # Moves to a flower
    if new_place.isdigit():
        collected_nectar += int(new_place)
    elif new_place == 'H':
        break

    if energy == 0 and collected_nectar < NECTAR_FOR_HONEY:
        break
    elif energy == 0 and collected_nectar >= NECTAR_FOR_HONEY and not is_restored:
        energy += collected_nectar - NECTAR_FOR_HONEY
        collected_nectar = NECTAR_FOR_HONEY
        is_restored = True
    elif energy == 0 and is_restored:
        break

if new_place == 'H' and collected_nectar >= 30:
    print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
elif new_place == 'H' and collected_nectar <= 30:
    print("Beesy did not manage to collect enough nectar.")
elif energy <= 0 and new_place != 'H':
    print("This is the end! Beesy ran out of energy.")

for row in matrix:
    print(*row, sep='')