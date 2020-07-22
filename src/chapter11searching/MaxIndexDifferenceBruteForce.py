''

def maxIndexDiff(A):
	maxDiff = -1
	maxJ = maxI = -1
	n = len(A)
	for i in range(0, n):
		j = n - 1
		while(j > i):
			if(A[j] > A[i] and maxDiff < (j - i)):
				maxDiff = j - i
				maxI = i
				maxJ = j
			j -= 1
	return maxDiff, maxI, maxJ
	
A = [34, 8, 10, 3, 2, 80, 30, 33, 1]
print maxIndexDiff(A)
