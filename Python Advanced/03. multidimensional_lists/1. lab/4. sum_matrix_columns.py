rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]


for column in range(columns):
    sum_columns = 0
    for row in range(rows):
        sum_columns += matrix[row][column]
    print(sum_columns)
