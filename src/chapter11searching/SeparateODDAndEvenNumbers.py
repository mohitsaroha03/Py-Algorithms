# Link: 
# IsDone: 0
def separateEvenOdd(A):
	left = 0; right = len(A) - 1
	while(left < right):
		while(A[left] % 2 == 0 and left < right):
			left += 1
		while(A[right] % 2 == 1 and left < right):
			right -= 1
		if(left < right):
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
A = [12, 34, 45, 9, 8, 90, 3]
separateEvenOdd(A)
print A
