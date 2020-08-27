# Link: https://www.geeksforgeeks.org/find-the-largest-rectangle-of-1s-with-swapping-of-columns-allowed/
# Python 3 program to find the largest 
# rectangle of 1's with swapping 
# of columns allowed. 
# TODO: pending
R = 3
C = 5

# Returns area of the largest 
# rectangle of 1's 
def maxArea(mat): 
	
	# An auxiliary array to store count 
	# of consecutive 1's in every column. 
	hist = [[0 for i in range(C + 1)] 
			for i in range(R + 1)] 

	# Step 1: Fill the auxiliary array hist[][] 
	for i in range(0, C, 1): 
		
		# First row in hist[][] is copy of 
		# first row in mat[][] 
		hist[0][i] = mat[0][i] 

		# Fill remaining rows of hist[][] 
		for j in range(1, R, 1): 
			if ((mat[j][i] == 0)): 
				hist[j][i] = 0
			else: 
				hist[j][i] = hist[j - 1][i] + 1

	# Step 2: Sort rows of hist[][] in 
	# non-increasing order 
	for i in range(0, R, 1): 
		count = [0 for i in range(R + 1)] 

		# counting occurrence 
		for j in range(0, C, 1): 
			count[hist[i][j]] += 1

		# Traverse the count array from 
		# right side 
		col_no = 0
		j = R 
		while(j >= 0): 
			if (count[j] > 0): 
				for k in range(0, count[j], 1): 
					hist[i][col_no] = j 
					col_no += 1

			j -= 1
			
	# Step 3: Traverse the sorted hist[][] 
	# to find maximum area 
	max_area = 0
	for i in range(0, R, 1): 
		for j in range(0, C, 1): 
			
			# Since values are in decreasing order, 
			# The area ending with cell (i, j) can 
			# be obtained by multiplying column number 
			# with value of hist[i][j] 
			curr_area = (j + 1) * hist[i][j] 
			if (curr_area > max_area): 
				max_area = curr_area 

	return max_area 

# Driver Code 
if __name__ == '__main__': 
	mat = [[0, 1, 0, 1, 0], 
		[0, 1, 0, 1, 1], 
		[1, 1, 0, 1, 0]] 
	print("Area of the largest rectangle is", 
								maxArea(mat)) 