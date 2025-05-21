rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary = sum([matrix[i][i] for i in range(rows)])
secondary = sum([matrix[i][-1 - i] for i in range(rows)])

print(abs(primary - secondary))