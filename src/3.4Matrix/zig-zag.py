# https://www.geeksforgeeks.org/print-matrix-in-zig-zag-fashion-from-the-last-column/?ref=rp

# Python program for traversing a matrix from column n-1 
import sys; 

# Function used for traversing over the given matrix 
def traverseMatrix(mat, n): 

	# Initial cell coordinates 
	cur_x = 0; cur_y = n - 1 

	# Variable used for keeping track of last move 
	prev_move = "" 

	# Variable used for keeping count 
	# of cells traversed till next move 
	move_cnt = 1 
	cell_cnt = 1 
	print(mat[cur_x][cur_y]) 

	while cell_cnt < n * n: 

		# odd numbered move [SINGLE VERTICAL / HORIZONTAL] 
		if move_cnt & 1: 

			# last move was made in north east direction 
			if prev_move == "NORTH_WEST" or prev_move == "" : 

				# move left 
				if cur_y != 0: 
					cur_y -= 1 
					prev_move = "LEFT" 
				
				# move down 
				else : 
					cur_x += 1 
					prev_move = "DOWN" 

			# last move was made in south east direction 
			else : 

				# move down 
				if(cur_x != n-1): 
					cur_x += 1 
					prev_move = "DOWN" 

				# move left 
				else : 
					cur_y -= 1 
					prev_move = "LEFT" 
			
			print(mat[cur_x][cur_y]) 
			cell_cnt += 1 

		# even numbered move / s [DIAGONAL / S] 
		else : 
			if (move_cnt >> 1) & 1: 

				# move south east 
				while cur_x < n - 1 and cur_y < n - 1: 
					cur_x += 1; cur_y += 1 
					prev_move = "SOUTH_EAST" 
					print(mat[cur_x][cur_y]) 
					cell_cnt += 1 
				
			else : 

				# move north west 
				while cur_x > 0 and cur_y > 0: 
					cur_x -= 1 ; cur_y -= 1 
					prev_move = "NORTH_WEST"; 
					print(mat[cur_x][cur_y]) 
					cell_cnt += 1 
				
		move_cnt += 1 

# Driver function 
if __name__ == '__main__': 

	# number of rows and columns 
	n = 5 

	# 5x5 matrix 
	mat =[ 
		[1, 2, 3, 4, 5], 
		[6, 7, 8, 9, 10], 
		[11, 12, 13, 14, 15], 
		[16, 17, 18, 19, 20], 
		[21, 22, 23, 24, 25] 
	] 

	traverseMatrix(mat, n) 
