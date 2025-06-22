presents = int(input())
n = int(input())

matrix = [input().split() for _ in range(n)]
count_nice_kids = 0
happy_kids = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            santa_pos = (i, j)
            matrix[i][j] = '-'
        elif matrix[i][j] == 'V':
            count_nice_kids += 1

possible_moves = {'down': (1, 0), 'up': (-1, 0), 'left': (0, -1), 'right': (0, 1)}

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    current_row = santa_pos[0] + possible_moves[command][0]
    if current_row < 0 or current_row > n - 1:
        continue
    current_col = santa_pos[1] + possible_moves[command][1]
    if current_col < 0 or current_col > n - 1:
        continue

    if matrix[current_row][current_col] == 'V':
        happy_kids += 1
        presents -= 1
    elif matrix[current_row][current_col] == 'C':
        for move in possible_moves:
            if presents <= 0:
                break
            next_row = current_row + possible_moves[move][0]
            next_col = current_col + possible_moves[move][1]
            if matrix[next_row][next_col] == 'V':
                happy_kids += 1
                presents -= 1
                matrix[next_row][next_col] = '-'
            elif matrix[next_row][next_col] == 'X':
                presents -= 1
                matrix[next_row][next_col] = '-'

    matrix[current_row][current_col] = '-'
    santa_pos = (current_row, current_col)

count_nice_kids_end = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'V':
            count_nice_kids_end += 1

if presents <= 0 and happy_kids < count_nice_kids:
    print("Santa ran out of presents!")
matrix[santa_pos[0]][santa_pos[1]] = 'S'
for row in matrix:
    print(*row)
if count_nice_kids_end <= 0:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {count_nice_kids_end} nice kid/s.")