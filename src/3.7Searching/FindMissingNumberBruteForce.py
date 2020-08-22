# Link: 
# IsDone: 0
def FindMissingNumber(A):
	n = len(A)
	for i in range(1, n + 1):
		found = 0
		for j in range(0, n):
			if(i == A[j]):
				found = 1
		if found == 0:
			print "Missing number is ", i

A = [8, 2, 1, 4, 6, 5, 7, 9]
FindMissingNumber(A)
