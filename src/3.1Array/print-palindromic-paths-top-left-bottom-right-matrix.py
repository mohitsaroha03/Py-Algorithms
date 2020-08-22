# Link: https://www.geeksforgeeks.org/print-palindromic-paths-top-left-bottom-right-matrix/
# Python 3 program to print all 
# palindromic paths from top left 
# to bottom right in a grid. 

def isPalin(str): 

	l = len(str) // 2
	for i in range( l) : 
		if (str[i] != str[len(str) - i - 1]): 
			return False
		
	return True

# i and j are row and column 
# indexes of current cell 
# (initially these are 0 and 0). 
def palindromicPath(str, a, i, j, m, n): 
		
	# If we have not reached bottom 
	# right corner, keep exlporing 
	if (j < m - 1 or i < n - 1) : 
		if (i < n - 1): 
			palindromicPath(str + a[i][j], a, 
							i + 1, j, m, n) 
		if (j < m - 1): 
			palindromicPath(str + a[i][j], a, 
							i, j + 1, m, n) 

	# If we reach bottom right corner, 
	# we check if the path used is 
	# palindrome or not. 
	else : 
		str = str + a[n - 1][m - 1] 
		if isPalin(str): 
			print(str) 

# Driver code 
if __name__ == "__main__": 
	
	arr = [[ 'a', 'a', 'a', 'b' ], 
		['b', 'a', 'a', 'a' ], 
		[ 'a', 'b', 'b', 'a' ]] 
	str = "" 
	palindromicPath(str, arr, 0, 0, 4, 3) 
