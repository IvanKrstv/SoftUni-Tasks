rows, columns = [int(x) for x in input().split()]

start = ord('a')

matrix = []

for i in range(rows):
    row_data = []
    first_letter = chr(start + i)
    for j in range(columns):
        middle_letter = chr(start + i + j)
        row_data.append(f'{first_letter}{middle_letter}{first_letter}')

    matrix.append(row_data)

for row in matrix:
    print(*row)
