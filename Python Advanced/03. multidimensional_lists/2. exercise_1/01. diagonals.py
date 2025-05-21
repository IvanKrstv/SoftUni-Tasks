rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

primary = [matrix[i][i] for i in range(rows)]
secondary = [matrix[i][-1 - i] for i in range(rows)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")
