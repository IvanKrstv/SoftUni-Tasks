rows, columns= [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
max_row = 0
max_col = 0
for i in range(rows - 2):
    for j in range(columns - 2):

        current_sum = 0

        for row in range(i, i + 3):
            for column in range(j, j + 3):
                current_sum += matrix[row][column]

        if current_sum > max_sum:
            max_sum = current_sum
            max_row = i
            max_col = j

sub_matrix = [matrix[row][max_col: max_col + 3] for row in range(max_row, max_row + 3)]
print(f"Sum = {max_sum}")
for r in sub_matrix:
    print(*r)