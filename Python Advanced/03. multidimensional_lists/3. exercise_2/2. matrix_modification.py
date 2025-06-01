rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

def add(mtx, r, c, value):
    mtx[r][c] += value
    return mtx

def subtract(mtx, r, c, value):
    mtx[r][c] -= value
    return mtx

while True:
    command = input()
    if command == 'END':
        break

    action = command.split()[0]
    row, column, value = (int(x) for x in command.split()[1:4])

    if row not in range(0, rows) or column not in range(0, rows):
        print("Invalid coordinates")
        continue

    if action == 'Add':
        matrix = add(matrix, row, column, value)
    elif action == 'Subtract':
        matrix = subtract(matrix, row, column, value)

for row in matrix:
    print(*row)