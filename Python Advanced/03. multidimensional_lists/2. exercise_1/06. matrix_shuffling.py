rows, columns= [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

def is_valid_position(r1, c1, r2, c2, rows, cols):
    return 0 <= r1 < rows and 0 <= c1 < cols and 0 <= r2 < rows and 0 <= c2 < cols


while True:
    command = input().split()
    if command[0] == 'END':
        break

    if command[0] != 'swap' or len(command) != 5:
        print("Invalid input!")
        continue
    coords = [int(x) for x in command[1:]]

    if is_valid_position(*coords, rows, columns):
        matrix[coords[0]][coords[1]], matrix[coords[2]][coords[3]] = matrix[coords[2]][coords[3]], matrix[coords[0]][coords[1]]
    else:
        print("Invalid input!")
        continue
    for row in matrix:
        print(*row)