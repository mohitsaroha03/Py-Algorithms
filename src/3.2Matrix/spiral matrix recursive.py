# https://www.techiedelight.com/print-matrix-spiral-order/
# Python3 program for the above approach 

# Function for printing matrix in spiral 
# form i, j: Start index of matrix, row 
# and column respectively m, n: End index 
# of matrix row and column respectively 
def printdata(arr, i, j, m, n): 
	
	# If i or j lies outside the matrix 
	if (i >= m or j >= n): 
		return; 
		
	# Print First Row 
	for p in range(i, n): 
		print(arr[i][p], ) 
		
	# Print Last Column 
	for p in range(i + 1, m): 
		print(arr[p][n - 1], ) 
		
	# Print Last Row, if Last and 
	# First Row are not same 
	if ((m - 1) != i): 
		for p in range(n - 2, j - 1, -1): 
			print(arr[m - 1][p], ) 
			
	# Print First Column, if Last and 
	# First Column are not same 
	if ((n - 1) != j): 
		for p in range(m - 2, i, -1): 
			print(arr[p][j], ) 
			
	printdata(arr, i + 1, j + 1, m - 1, n - 1) 

# Driver code 
R = 4
C = 4
arr = [ [ 1, 2, 3, 4 ], 
		[ 5, 6, 7, 8 ], 
		[ 9, 10, 11, 12 ], 
		[ 13, 14, 15, 16 ] ] 
		
printdata(arr, 0, 0, R, C) 