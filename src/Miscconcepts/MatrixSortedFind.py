# Link: 
# IsDone: 0
def matrix_find(matrix, value):
    m = len(matrix)
    if m == 0:
        return 0

    n = len(matrix[0])
    if n == 0:
        return 0

    i = 0
    j = n - 1

    while i < m and j >= 0:
        if matrix[i][j] == value:
            return 1

        elif matrix[i][j] < value:
            i = i + 1

        else:
            j = j - 1

    return 0
