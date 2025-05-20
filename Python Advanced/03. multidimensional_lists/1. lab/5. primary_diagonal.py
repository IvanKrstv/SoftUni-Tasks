rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
sum_diagonal = 0

for i in range(rows):
    for j in range(rows):
        if i == j:
            sum_diagonal += matrix[i][j]

print(sum_diagonal)