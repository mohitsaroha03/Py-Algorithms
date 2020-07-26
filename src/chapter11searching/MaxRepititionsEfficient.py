# Link: 
# IsDone: 0
def MaxRepititionsEfficient(A):
	n = len(A)
	max = 0
	for i in range(0, len(A)):
		A[A[i] % n] += n
	for i in range(0, len(A)):
		 if(A[i] / n > max): 
			max = A[i] / n
			maxIndex = i
	print maxIndex, "repeated for ", max, " times"
A = [3, 2, 2, 3, 2, 2, 2, 3, 3]
MaxRepititionsEfficient(A)
