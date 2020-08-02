# https://www.techiedelight.com/print-matrix-spiral-order/
# Python 3 program to print matrix downward 

def printMatrixDiagonallyDown(matrix,n): 
	# printing elements above and on 
	# second diagonal 
	for k in range(n): 
		# traversing downwards starting 
		# from first row 
		row = 0
		col = k 
		while (col >= 0): 
			print(matrix[row][col]) 
			row += 1
			col -= 1

	# printing elements below second 
	# diagonal 
	for j in range(1,n): 
		# traversing downwards starting 
		# from last column 
		col = n - 1
		row = j 
		while (row < n): 
			print(matrix[row][col]) 
			row += 1
			col -= 1

if __name__ == '__main__': 
	matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]] 
	n = 3
	printMatrixDiagonallyDown(matrix, n) 
