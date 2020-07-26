#

def findPivot1(A):
	for i in range(len(A)):
		leftSum = sum(A[:i])
		rightSum = sum(A[i+1:])
		if leftSum == rightSum:
			return A[i]

def findPivot2(A):
	S= sum(A)
	leftSum = 0
	for i in range(len(A)):
		if leftSum == S-A[i]-leftSum:
			return A[i]		
		leftSum += A[i]

print findPivot2([12,6,9,3,5,2,1,9,10])
