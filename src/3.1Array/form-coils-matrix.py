# Link: https://www.geeksforgeeks.org/form-coils-matrix/
# Python3 program to pr2 coils of a 
# 4n x 4n matrix. 
# TODO: pending
# Prcoils in a matrix of size 4n x 4n 
def printCoils(n): 
	
	# Number of elements in each coil 
	m = 8*n*n 
	
	# Let us fill elements in coil 1. 
	coil1 = [0]*m 
	
	# First element of coil1 
	# 4*n*2*n + 2*n 
	coil1[0] = 8*n*n + 2*n 
	
	curr = coil1[0] 
	
	nflg = 1
	step = 2
	
	# Fill remaining m-1 elements in coil1[] 
	index = 1
	while (index < m): 
		
		# Fill elements of current step from 
		# down to up 
		for i in range(step): 
			
			# Next element from current element 
			curr = coil1[index] = (curr - 4*n*nflg) 
			index += 1
			if (index >= m): 
				break
		if (index >= m): 
			break
		
		# Fill elements of current step from 
		# up to down. 
		for i in range(step): 
			
			curr = coil1[index] = curr + nflg 
			index += 1
			if (index >= m): 
				break
		nflg = nflg*(-1) 
		step += 2
	
	#get coil2 from coil1 */ 
	
	coil2 = [0]*m 
	i = 0
	while(i < 8*n*n): 
		coil2[i] = 16*n*n + 1 -coil1[i] 
		i += 1
	# Prboth coils 
	print("Coil 1 :", end = " ") 
	i = 0
	while(i < 8*n*n): 
		print(coil1[i], end = " ") 
		i += 1
	print("\nCoil 2 :", end = " ") 
	i = 0
	while(i < 8*n*n): 
		print(coil2[i], end = " ") 
		i += 1

# Driver code 

n = 1
printCoils(n) 
