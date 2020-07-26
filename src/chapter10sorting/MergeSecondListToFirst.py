# Link: 
# IsDone: 0
def Merge(A, m, B, n):
	i = n - 1
	j = k = m - 1
	while k >= 0:
		if(B[i] > A[j] or j < 0):
			A[k] = B[i]
			i -= 1
			if(i < 0):
				break
		else:
			A[k] = A[j]
			j -= 1
		k -= 1
