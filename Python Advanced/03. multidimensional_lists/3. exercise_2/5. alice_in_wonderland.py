n = int(input())

matrix = []
alice_pos = ()

for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == 'A':
            alice_pos = (i, j)
            matrix[i][j] = '*'

possible_moves = {'down': (1, 0), 'up': (-1, 0), 'left': (0, -1), 'right': (0, 1)}

tea_bags = 0

current_row = alice_pos[0]
current_col = alice_pos[1]
while tea_bags < 10:
    command = input()
    current_row += possible_moves[command][0]
    current_col += possible_moves[command][1]

    if not 0 <= current_row < n or not 0 <= current_col < n:
        break

    if matrix[current_row][current_col] == 'R':
        matrix[current_row][current_col] = '*'
        break

    if matrix[current_row][current_col].isdigit():
        tea_bags += int(matrix[current_row][current_col])

    matrix[current_row][current_col] = '*'


if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row)