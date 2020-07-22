''

def maxSumWithNoTwoContinuousNumbers(A):
	n = len(A)
	M = [0] * (n + 1)
	M[0] = A[0]
	
	if(A[0] > A[1]): 
		 M[0] = A[0]
	else: M[0] = A[1]
	for i in range(2, n): 
		if(M[i - 1] > M[i - 2] + A[i]):
			M[i] = M[i - 1]
		else: 	M[i] = M[i - 2] + A[i]	

	return M[n - 1]
	
A = [-2, 3, -16, 100, -4, 5]
print maxSumWithNoTwoContinuousNumbers(A)
A = [-2, 11, -4, 13, -5, 2 ]
print maxSumWithNoTwoContinuousNumbers(A)
A = [-15, -23, -476, -3, -292]
print maxSumWithNoTwoContinuousNumbers(A)
