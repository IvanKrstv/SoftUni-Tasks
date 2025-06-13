n = int(input())

matrix = [input().split() for _ in range(n)]

STARS_GOAL = 10
collected_stars = 2
player_pos = (0, 0)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'P':
            player_pos = (i, j)
matrix[player_pos[0]][player_pos[1]] = '.'

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while 0 < collected_stars < 10:
    command = input()

    current_row = player_pos[0] + moves[command][0]
    current_col = player_pos[1] + moves[command][1]

    if current_row not in range(n) or current_col not in range(n):
        current_row = current_col = 0

    if matrix[current_row][current_col] == '*':
        collected_stars += 1
        matrix[current_row][current_col] = '.'
        player_pos = (current_row, current_col)
    elif matrix[current_row][current_col] == '#':
         collected_stars -= 1
    elif matrix[current_row][current_col]:
        player_pos = (current_row, current_col)

if collected_stars == 10:
    print("You won! You have collected 10 stars.")
elif collected_stars == 0:
    print("Game over! You are out of any stars.")
print(f"Your final position is [{player_pos[0]}, {player_pos[1]}]")
matrix[player_pos[0]][player_pos[1]] = 'P'
for row in matrix:
    print(*row)