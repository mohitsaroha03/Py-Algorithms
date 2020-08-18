# Link: https://www.geeksforgeeks.org/number-of-paths-with-exactly-k-coins/
# IsDone: 1

# A Naive Recursive Python program to 
# count paths with exactly 'k' coins 

R = 3
C = 3

# Recursive function to count paths 
# with sum k from (0, 0) to (m, n) 
def pathCountRec(mat, m, n, k): 

	# Base cases 
	if m < 0 or n < 0: 
		return 0
	elif m == 0 and n == 0: 
		return k == mat[m][n] 

	# #(m, n) can be reached either 
	# through (m-1, n) or through 
	# (m, n-1) 
	return (pathCountRec(mat, m-1, n, k-mat[m][n]) 
		+ pathCountRec(mat, m, n-1, k-mat[m][n])) 

# A wrapper over pathCountRec() 
def pathCount(mat, k): 
	return pathCountRec(mat, R-1, C-1, k) 

# Driver Program 
k = 12
mat = [[1, 2, 3], 
	[4, 6, 5], 
	[3, 2, 1]] 

print(pathCount(mat, k)) 
