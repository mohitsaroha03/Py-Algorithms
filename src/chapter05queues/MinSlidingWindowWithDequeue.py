# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

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

def printMax(arr, n, k): 
    max = 0
    
    for i in range(n - k + 1): 
        max = arr[i] 
        for j in range(1, k): 
            if arr[i + j] > max: 
                max = arr[i + j] 
        print str(max) + " "
  
# Driver method 
if __name__=="__main__": 
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    n = len(arr) 
    k = 3
    printMax(arr, n, k) 
