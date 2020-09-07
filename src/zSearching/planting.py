#

def planting(A, K):
	counter = 0
	for i in range(0,len(A)):
		if (A[i] == 0 and (i == 0 or A[i-1] ==0) and ( i == len(A)-1 or A[i+1] == 0)):
			A[i] = 1
			counter += 1
			if counter == K:
				return True, A
	return False

print planting([1,0,0,0,1,0,0], 2)
print planting([1,0,0,0,1,0,0], 3)
