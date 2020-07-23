# isGFG: , Link: 
# IsDone: 0
def separateZerosAndOnes(A):
	left = 0; right = len(A) - 1
	while(left < right):
		while(A[left] == 0 and left < right):
			left += 1
		while(A[right] == 1 and left < right):
			right -= 1
		if(left < right):
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
A = [1, 1, 0, 0, 1, 0, 1]
separateZerosAndOnes(A)
print A
