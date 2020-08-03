# link: https://www.geeksforgeeks.org/traverse-a-given-matrix-using-recursion/?ref=rp
# Python3 program to traverse the matrix recursively 
N = 2
M = 3

# Function to traverse the matrix recursively 
def traverseMatrix(arr, current_row, current_col) : 

	# If the entire column is traversed 
	if (current_col >= M) : 
		return 0; 

	# If the entire row is traversed 
	if (current_row >= N) : 
		return 1; 

	# Print the value of the current 
	# cell of the matrix 
	print(arr[current_row][current_col]); 

	# Recursive call to traverse the matrix 
	# in the Horizontal direction 
	if (traverseMatrix(arr, current_row, current_col + 1 ) == 1) : 
		return 1; 
		
	# Recursive call for changing the 
	# Row of the matrix 
	return traverseMatrix(arr, current_row + 1, 0); 

# Driver code 
if __name__ == "__main__" : 
	arr = [ [ 1, 2, 3 ], 
			[ 4, 5, 6 ] ]; 

	traverseMatrix(arr, 0, 0); 
