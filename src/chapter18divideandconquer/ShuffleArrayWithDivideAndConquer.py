# Link: 
# IsDone: 0
def shuffleArray(A, l, r):
	# Array center
	c = l + (r - l) / 2
	q = 1 + l + (c - l) / 2
	if(l == r):  # Base case when the array has only one element
		return
	k = 1
	I = q
	while(i <= c):	
		# Swap elements around the center
		tmp = A[i]	
		A[i] = A[c + k]
		A[c + k] = tmp
		i += 1
		k += 1
	
	ShuffleArray(A, l, c)  # Recursively call the function on the left and right
	ShuffleArray(A, c + 1, r)  # Recursively call the function on the right
