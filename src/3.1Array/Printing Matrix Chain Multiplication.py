# Link: https://www.geeksforgeeks.org/printing-brackets-matrix-chain-multiplication-problem/
# https://www.geeksforgeeks.org/printing-matrix-chain-multiplication-a-space-optimized-solution/
# A space optimized python3 program to 
# print optimal parenthesization in 
# matrix chain multiplication. 

def printParenthesis(m, j, i ): 

	# Displaying the parenthesis. 
	if j == i: 

		# The first matrix is printed as 
		# 'A', next as 'B', and so on 
		print(chr(65 + j), end = "") 
		return; 
	else: 
		print("(", end = "") 

		# Passing (m, k, i) instead of (s, i, k) 
		printParenthesis(m, m[j][i] - 1, i) 

		# (m, j, k+1) instead of (s, k+1, j) 
		printParenthesis(m, j, m[j][i]) 
		print (")", end = "" ) 

def matrixChainOrder(p, n): 

	# Creating a matrix of order 
	# n*n in the memory. 
	m = [[0 for i in range(n)] 
			for i in range (n)] 

	for l in range (2, n + 1): 
		for i in range (n - l + 1): 
			j = i + l - 1

			# Initializing infinity value. 
			m[i][j] = float('Inf') 
			for k in range (i, j): 
				q = (m[i][k] + m[k + 1][j] +
					(p[i] * p[k + 1] * p[j + 1])); 
				if (q < m[i][j]): 
					m[i][j] = q 

					# Storing k value in opposite index. 
					m[j][i] = k + 1
	return m; 

# Driver Code 
arr = [40, 20, 30, 10, 30] 
n = len(arr) - 1

m = matrixChainOrder(arr, n) # Forming the matrix m 

print("Optimal Parenthesization is: ", end = "") 

# Passing the index of the bottom left 
# corner of the 'm' matrix instead of 
# passing the index of the top right 
# corner of the 's' matrix as we used 
# to do earlier. Everything is just opposite 
# as we are using the bottom half of the 
# matrix so assume everything opposite even 
# the index, take m[j][i]. 
printParenthesis(m, n - 1, 0) 
print("\nOptimal Cost is :", m[0][n - 1]) 
