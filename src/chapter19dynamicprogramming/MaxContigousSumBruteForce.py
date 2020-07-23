# isGFG: , Link: 
# IsDone: 0
def MaxContigousSum(A):
	maxSum = 0
	n = len(A)
	for i in range(1, n): 	
		for j in range(i, n):	
			currentSum = 0
			for k in range(i, j + 1):	
				currentSum += A[k]
				if(currentSum > maxSum):
					maxSum = currentSum

	return maxSum;

A = [-2, 3, -16, 100, -4, 5]
print MaxContigousSum(A)
A = [-2, 11, -4, 13, -5, 2 ]
print MaxContigousSum(A)
A = [-15, -23, -476, -3, -292]
print MaxContigousSum(A)
