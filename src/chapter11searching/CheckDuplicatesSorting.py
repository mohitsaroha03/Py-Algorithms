# Link: 
# IsDone: 0
def CheckDuplicatesSorting(A):
	A.sort()
	for i in range(0, len(A) - 1):
		if(A[i] == A[i + 1]):
			print("Duplicates exist:", A[i])
			return
	print("No duplicates in given array.")

A = [33, 2, 10, 20, 22, 32]
CheckDuplicatesSorting(A)
A = [3, 2, 1, 2, 2, 3]
CheckDuplicatesSorting(A)
