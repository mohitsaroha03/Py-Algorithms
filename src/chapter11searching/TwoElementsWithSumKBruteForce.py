# isGFG: , Link: 
# IsDone: 0
def twoElementsWithSumKBruteForce(A, K):
	n = len(A)
    	for i in range(0, n):
		for j in range(i + 1, n):
			if(A[i] + A[j] == K):
				return 1
	return 0
    
A = [1, 4, 45, 6, 10, -8]
A.sort()
print twoElementsWithSumKBruteForce(A, 111)
