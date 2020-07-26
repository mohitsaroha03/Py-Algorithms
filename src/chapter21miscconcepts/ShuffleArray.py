# Link: 
# IsDone: 0
import random
def shuffle_array(A):
	n = len(A)
	i = n - 1
	while i > 0:
		j = int((random.random()) % (i + 1))
		tmp = A[j - 1];A[j - 1] = A[j];A[j] = tmp
		i -= 1

A = [1, 3, 5, 6, 2, 4, 6, 8]
shuffle_array(A)
print A
