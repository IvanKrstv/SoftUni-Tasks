rows = int(input())

matrix = [list(input()) for _ in range(rows)]
symbol = input()

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == symbol:
            print((i, j))
            exit()

print(f"{symbol} does not occur in the matrix")