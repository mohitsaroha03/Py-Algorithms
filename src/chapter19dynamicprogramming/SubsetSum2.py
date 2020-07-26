# Link: 
# IsDone: 0
def SubsetSum2(A):
	n = len(A)
	K = 0
	for i in range(0, n): 
		K += A[i]
	A.sort()
	T = [0] * (K + 1)
	T[0] = 1
	R = 0
	# process the numbers one by one
	for i in range(0, n): 
		for j in range(R, -1, -1): 
			if(T[j]): 
				T[j + A[i]] = 1
			R = min(K / 2, R + A[i])
	
	return T[K / 2]
	
A = [3, 2, 4, 19, 3, 7, 13, 10, 6, 11]

print SubsetSum2(A)
