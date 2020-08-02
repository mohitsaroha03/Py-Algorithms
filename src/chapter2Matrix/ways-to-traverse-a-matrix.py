# https://www.geeksforgeeks.org/count-the-number-of-ways-to-traverse-a-matrix/?ref=rp
# Python 3 program using recursive solution to count 
# number of ways to reach mat[m-1][n-1] from 
# mat[0][0] in a matrix mat[][] 

# Returns The number of way from top-left 
# to mat[m-1][n-1] 
def countPaths(m, n) : 

	# Return 1 if it is the first row or 
	# first column 
	if m == 1 or n == 1 : 
		return 1

	# Recursively find the no of way to 
	# reach the last cell. 
	return (countPaths(m - 1, n) +
			countPaths(m, n - 1)) 


# Driver code	 
if __name__ == "__main__" : 

	n = 5
	m = 5
	print(countPaths(n, m)) 