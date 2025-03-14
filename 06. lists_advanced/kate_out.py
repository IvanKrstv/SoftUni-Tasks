rows = int(input())
matrix = []
visited = []
def can_go_left(mat: list, row: int, column: int) -> bool:
    if column - 1 < 0 or mat[row][column - 1] == " ":
        return True
    return False

def can_go_right(mat: list, row: int, column: int) -> bool:
    if column + 1 == len(matrix[row]) or mat[row][column + 1] == " ":
        return True
    return False

def can_go_down(mat: list, row: int, column: int) -> bool:
    if row + 1 == rows or mat[row + 1][column] == " ":
        return True
    return False

def can_go_up(mat: list, row: int, column: int) -> bool:
    if row - 1 < 0 or mat[row - 1][column] == " ":
        return True
    return False

for i in range(rows):
    current_row = list(input())
    matrix.append(current_row)
    for column in range(len(current_row)):
        if matrix[i][column] == "k":
            row_kate = i
            column_kate = column

number_of_moves = 0

while 0 <= row_kate <= rows - 1 and 0 <= column_kate <= len(matrix[0]):
    if can_go_down(matrix, row_kate, column_kate) and [row_kate + 1, column_kate] not in visited:
        row_kate += 1
    elif can_go_up(matrix, row_kate, column_kate) and [row_kate - 1, column_kate] not in visited:
        row_kate -= 1
    elif can_go_left(matrix, row_kate, column_kate) and [row_kate, column_kate - 1] not in visited:
        column_kate -= 1
    elif can_go_right(matrix, row_kate, column_kate) and [row_kate, column_kate + 1] not in visited:
        column_kate += 1
    else:
        print("Kate cannot get out")
        exit()
    number_of_moves += 1
    visited.append([row_kate, column_kate])

print(f"Kate got out in {number_of_moves} moves")