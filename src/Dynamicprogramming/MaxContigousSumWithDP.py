# Link: 
# IsDone: 0
def MaxContigousSum(A):
	maxSum = 0
	n = len(A)
	M = [0] * (n + 1)
	if(A[0] > 0): 
		 M[0] = A[0]
	else: M[0] = 0
	for i in range(1, n): 
		if(M[i - 1] + A[i] > 0):
			M[i] = M[i - 1] + A[i]
		else: 	M[i] = 0		

	for i in range(0, n): 
		if(M[i] > maxSum):
			maxSum = M[i]

	return maxSum
	
A = [-2, 3, -16, 100, -4, 5]
print MaxContigousSum(A)
A = [-2, 11, -4, 13, -5, 2 ]
print MaxContigousSum(A)
A = [-15, -23, -476, -3, -292]
print MaxContigousSum(A)
