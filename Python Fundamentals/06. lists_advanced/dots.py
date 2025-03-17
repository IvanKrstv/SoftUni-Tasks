rows = int(input())
matrix = []
point_coordinates = []
visited_points = []

for row in range(rows):
    current_row = input().split()
    for element in current_row:
        if element == ".":
            point_coordinates.append([row, current_row.index(element)])
    matrix.append(current_row)

# Get a point
# Check if it can be connected to another
# If possible do the checks for the next point
# Do that while there is no point you can connect to