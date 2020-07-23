# isGFG: , Link: 
# IsDone: 0
def FindMissingNumber(A):
	n = len(A)
	X = 0
	for i in range(1, n + 2):
		X = X ^ i
	for i in range(0, n):
		X = X ^ A[i]
	print "Missing number is ", X
A = [8, 2, 1, 4, 6, 5, 7, 9]
FindMissingNumber(A)
