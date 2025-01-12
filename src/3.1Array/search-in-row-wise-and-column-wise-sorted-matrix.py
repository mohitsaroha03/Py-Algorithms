# Link: https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/
# Python3 program to search an element 
# in row-wise and column-wise sorted matrix 

# Searches the element x in mat[][]. If the 
# element is found, then prints its position 
# and returns true, otherwise prints "not found" 
# and returns false 
def search(mat, n, x): 

	i = 0
	
	# set indexes for top right element 
	j = n - 1
	while ( i < n and j >= 0 ): 
	
		if (mat[i][j] == x ): 
	
			print("n Found at ", i, ", ", j) 
			return 1
	
		if (mat[i][j] > x ): 
			j -= 1
			
		# if mat[i][j] < x 
		else: 
			i += 1
	
	print("Element not found") 
	return 0 # if (i == n || j == -1 ) 

# Driver Code 
mat = [ [10, 20, 30, 40], 
		[15, 25, 35, 45], 
		[27, 29, 37, 48], 
		[32, 33, 39, 50] ] 
search(mat, 4, 29) 