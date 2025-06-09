def num_triangle(n: int):
    for i in range(1, n + 1):
        row = [num for num in range(1, i + 1)]
        print(*row)
    for i in range(n - 1, 0, -1):
        row = [num for num in range(1, i + 1)]
        print(*row)