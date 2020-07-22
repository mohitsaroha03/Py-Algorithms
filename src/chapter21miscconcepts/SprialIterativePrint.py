''

def spiral_iterative(n):
    dx, dy = 1, 0  # Starting increments
    x, y = 0, 0  # Starting location
    matrix = [[None] * n for j in range(n)]
    for i in xrange(n ** 2):
        matrix[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return matrix
 
def print_spiral(matrix):
    n = range(len(matrix))
    for y in n:
        for x in n:
            print "%2i" % matrix[x][y],
        print
 
print_spiral(spiral_iterative(5))
