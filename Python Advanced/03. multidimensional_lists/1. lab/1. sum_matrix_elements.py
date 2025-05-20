rows, columns = [int(x) for x in input().split(', ')]
matrix = []
sum_elements = 0

for i in range(rows):
    row_data = [int(x) for x in input().split(', ')]
    sum_elements += sum(row_data)
    matrix.append(row_data)

print(sum_elements)
print(matrix)