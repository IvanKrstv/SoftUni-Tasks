rows, columns= [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]
squares = 0

for i in range(rows - 1):
    for j in range(columns - 1):
        current_element = matrix[i][j]
        right_element = matrix[i][j + 1]
        bottom_element = matrix[i + 1][j]
        bottom_right_element = matrix[i + 1][j + 1]

        if current_element == right_element == bottom_element == bottom_right_element:
            squares += 1

print(squares)