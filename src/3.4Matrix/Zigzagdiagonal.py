# Link: https://www.geeksforgeeks.org/zigzag-tree-traversal/
# IsDone: 1
# Python3 program to print all elements 
# of given matrix in diagonal order 
ROW = 5
COL = 4

# Main function that prints given 
# matrix in diagonal order 
def diagonalOrder(matrix) : 
	
	# There will be ROW+COL-1 lines in the output 
	for line in range(1, (ROW + COL)) : 
		# Get column index of the first element 
		# in this line of output. The index is 0 
		# for first ROW lines and line - ROW for 
		# remaining lines 
		start_col = max(0, line - ROW) 

		# Get count of elements in this line. 
		# The count of elements is equal to 
		# minimum of line number, COL-start_col and ROW 
		count = min(line, (COL - start_col), ROW) 

		# Print elements of this line 
		for j in range(0, count) : 
			print(matrix[min(ROW, line) - j - 1] 
						[start_col + j]) 

		print() 
	
	
# Utility function to print a matrix 
def printMatrix(matrix) : 
	for i in range(0, ROW) : 
		for j in range(0, COL) : 
			print(matrix[i][j]) 
			
		print() 
		

# Driver COde 
M = [ [1, 2, 3, 4], 
	[5, 6, 7, 8], 
	[9, 10, 11, 12], 
	[13, 14, 15, 16], 
	[17, 18, 19, 20] ] 
print("Given matrix is ") 
printMatrix(M) 

print ("\nDiagonal printing of matrix is ") 
diagonalOrder(M) 


