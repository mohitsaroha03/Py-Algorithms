# Link - https://leetcode.com/problems/01-matrix/
# https://www.geeksforgeeks.org/distance-nearest-cell-1-binary-matrix/

from collections import deque
class Solution:
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(self, matrix, i, j):
        q = deque([(i, j)])
        dist = 0
        while q:
            q_size = len(q)
            for _ in range(q_size):
                x, y = q.popleft()
                if matrix[x][y] == 0:
                    return dist

                for m_x, m_y in self.moves:
                    next_x = x + m_x
                    next_y = y + m_y
                    if self.is_inside(next_x, next_y):
                        q.append((next_x, next_y))
            dist += 1

    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])

        self.is_inside = lambda x, y: not(x < 0 or y < 0 or x >= m or y >= n)

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = self.bfs(matrix, i, j)

        return res
mat = [[0,0,0],
 [0,1,0],
 [1,1,1]]
s = Solution()
print (s.updateMatrix(mat))