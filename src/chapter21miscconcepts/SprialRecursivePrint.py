# Link: 
# IsDone: 0
def spiral(n):
    def spiralPart(x, y, n):
        if x == -1 and y == 0:
            return -1
        if y == (x + 1) and x < (n // 2):
            return spiralPart(x - 1, y - 1, n - 1) + 4 * (n - y)
        if x < (n - y) and y <= x:
            return spiralPart(y - 1, y, n) + (x - y) + 1
        if x >= (n - y) and y <= x:
            return spiralPart(x, y - 1, n) + 1
        if x >= (n - y) and y > x:
            return spiralPart(x + 1, y, n) + 1
        if x < (n - y) and y > x:
            return spiralPart(x, y - 1, n) - 1
 
    array = [[0] * n for j in xrange(n)]
    for x in xrange(n):
        for y in xrange(n):
            array[x][y] = spiralPart(y, x, n)
    return array
 
for row in spiral(5):
    print " ".join("%2s" % x for x in row)
