def fill_the_box(*args):
    height, length, width = args[0:3]

    size = height * length * width
    current_box = 0

    for arg in args[3:]:
        if arg == 'Finish':
            break
        current_box += arg

    if size > current_box:
        return f"There is free space in the box. You could put {size - current_box} more cubes."
    elif size < current_box:
        return f"No more free space! You have {current_box - size} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))