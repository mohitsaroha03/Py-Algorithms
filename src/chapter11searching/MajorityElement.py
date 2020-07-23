# isGFG: , Link: 
# IsDone: 0
def majorityElement(A):
	count = 0
	element = -1
	n = len(A)
	if n == 0:
		return
	for i in range(0, n - 1):
		if(count == 0) :
			element = A[i]
			count = 1
		elif(element == A[i]):
			count += 1
		else:
			count -= 1
	return element

A = [7, 3, 2, 3, 3, 6, 3	]
print majorityElement(A)
