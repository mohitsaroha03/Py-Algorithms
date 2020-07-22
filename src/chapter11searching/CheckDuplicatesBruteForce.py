''

def CheckDuplicatesBruteForce(A):
	for i in range(0, len(A)):
		for j in range(i + 1, len(A)):
			if(A[i] == A[j]):
				print("Duplicates exist:", A[i])
				return;
	print("No duplicates in given array.")

A = [3, 2, 10, 20, 22, 32]
CheckDuplicatesBruteForce(A)
A = [3, 2, 1, 2, 2, 3]
CheckDuplicatesBruteForce(A)
