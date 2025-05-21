from collections import deque

rows, columns = [int(x) for x in input().split()]
string = deque(input())

matrix = []

for row in range(rows):
    matrix.append([''] * columns)
    for col in range(columns):
        if row % 2 == 0:
            matrix[row][col] = string[0]
        else:
            matrix[row][-1 - col] = string[0]
        string.rotate(-1)

[print(*row, sep='') for row in matrix]