# Link: 
# IsDone: 0
from collections import deque
 
def MinSlidingWindow(A, k):
    D = deque()
    res, i = [], 0
    for i in xrange(len(A)):
        while D and D[-1][0] >= A[i]:
            D.pop()
        D.append((A[i], i + k - 1))
        if i >= k - 1: res.append(D[0][0])
        if i == D[0][1]: D.popleft()
    return res
 
print MinSlidingWindow([4, 3, 2, 1, 5, 7, 6, 8, 9], 3)
