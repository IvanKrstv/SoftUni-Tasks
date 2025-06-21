n = int(input())
matrix = [list(input()) for _ in range(n)]
ship_pos = (0, 0)
remaining_treasures = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            ship_pos = (i, j)
            matrix[i][j] = '.'
        elif matrix[i][j] == '*':
            remaining_treasures += 1

durability = 100

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
used_charm = False

while True:
    command = input()
    if command == 'stop':
        break

    current_row = ship_pos[0] + moves[command][0]
    if current_row >= n:
        current_row = 0
    elif current_row < 0:
        current_row = n - 1
    current_col = ship_pos[1] + moves[command][1]
    if current_col >= n:
        current_col = 0
    elif current_col < 0:
        current_col = n - 1

    if matrix[current_row][current_col] == '*':
        remaining_treasures -= 1
    elif matrix[current_row][current_col] == 'C':
        if not used_charm:
            used_charm = True
            durability += 25
            if durability > 100:
                durability = 100
    elif matrix[current_row][current_col] == 'M':
        durability -= 25
    matrix[current_row][current_col] = '.'
    ship_pos = (current_row, current_col)
    if remaining_treasures == 0:
        print("Yo-ho-ho! All treasure chests collected!")
        break
    if durability <= 0:
        print(f"Shipwreck! Last known coordinates ({ship_pos[0]}, {ship_pos[1]})")
        break

if remaining_treasures > 0 and durability > 0:
    print("Retreat! Some treasures remain unclaimed.")
print(f"Ship Durability: {durability}")
if remaining_treasures > 0:
    print(f"Unclaimed chests: {remaining_treasures}")
matrix[ship_pos[0]][ship_pos[1]] = 'S'
for row in matrix:
    print(*row, sep='')