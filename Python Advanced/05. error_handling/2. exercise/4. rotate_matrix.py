class MatrixContentError(Exception):
    """The matrix contains non-integer values"""
    pass

class MatrixSizeError(Exception):
    """The size of the matrix is not a square"""
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

mtrx = []

while True:
    line = input().split()

    if not line:
        break

    for num in line:
        if not num.isdigit():
            raise MatrixContentError("The matrix must consist of only integers")

    mtrx.append(line)

for row in mtrx:
    if len(mtrx) != len(row):
        raise MatrixSizeError("The size of the matrix is not a perfect square")


rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')
