# isGFG: , Link: 
# IsDone: 0
def threeElementsWithSumKWithSorting(A, K):
	n = len(A)
	left = 0
	right = n - 1
	for i in range(0, n - 2):
		left = i + 1
		right = n - 1
		while(left < right):
			print A[i] + A[left] + A[right], K
			if(A[i] + A[left] + A[right] == K):
				print "yes-->", A[i], " + ", A[left], " + ", A[right], " = ", K		
				return 1
			elif(A[i] + A[left] + A[right] < K):
				left += 1
			else:
				right -= 1
	return 0
    
A = [1, 6, 45, 4, 10, 18]
A.sort()
print threeElementsWithSumKWithSorting(A, 23)
