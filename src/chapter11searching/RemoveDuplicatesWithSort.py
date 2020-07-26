# Link: 
# IsDone: 0
def RemoveDuplicates(A):
	A.sort()
	print A
	j = 0
	for i in range(1, len(A)):
		if (A[j] != A[i]):
			j += 1
			A[j] = A[i]
			
			
	print A[:j + 1]

A = [54, 31, 93, 54, 77, 31, 44, 55, 93]
RemoveDuplicates(A)
