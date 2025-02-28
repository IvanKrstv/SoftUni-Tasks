rows = int(input())
matrix = []
visited = []

row_kate = None
column_kate = None

# Input the maze
for i in range(rows):
    current_row = list(input())
    matrix.append(current_row)

    if row_kate is not None and column_kate is not None: # No point of the next loop if the initial position is found
        continue

    # Find Kate's starting position
    for column in range(len(current_row)):
        if matrix[i][column] == "k":
            row_kate = i
            column_kate = column

if row_kate == 0 or row_kate == rows - 1 or column_kate == 0 or column_kate == len(matrix[0]) - 1:
    print("Kate got out in 0 moves")
    exit()

# Directions: (down, up, right, left)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# DFS function to explore the maze
def dfs(row: int, col: int, moves: int) -> int:
    if row < 0 or row >= rows or col < 0 or col >= len(matrix[0]) or matrix[row][col] == "#":
        return -1  # Invalid move

    # If Kate is on the border, and it's an empty space, she can escape
    if (row == 0 or row == rows - 1 or col == 0 or col == len(matrix[0]) - 1) and matrix[row][col] == " ":
        return moves + 1  # Kate reached an exit, return the number of moves + 1 to exit properly

    visited.append((row, col))  # Mark the current cell as visited
    max_moves = -1  # Track the longest path

    # Explore all directions
    for direction_row, direction_column in directions:
        new_row, new_col = row + direction_row, col + direction_column

        if (new_row, new_col) not in visited:
            result = dfs(new_row, new_col, moves + 1)
            if result != -1:
                if result > max_moves:
                    max_moves = result

    visited.remove((row, col))  # Unmark the cell after exploring all paths
    return max_moves


# Start DFS from Kate's position
result = dfs(row_kate, column_kate, 0)

if result == -1: # There were no possible routes
    print("Kate cannot get out")
else:
    print(f"Kate got out in {result} moves")
