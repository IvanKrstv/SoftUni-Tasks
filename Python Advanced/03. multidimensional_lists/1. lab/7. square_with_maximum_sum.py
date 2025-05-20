rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

max_sum = float('-inf')
sub_matrix = []
for i in range(rows - 1):
    for j in range(columns - 1):
        current_element = matrix[i][j]
        right_element = matrix[i][j + 1]
        bottom_element = matrix[i + 1][j]
        bottom_right_element = matrix[i + 1][j + 1]

        current_sum = (current_element + right_element
                       + bottom_element + bottom_right_element)

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_element, right_element], [bottom_element, bottom_right_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)