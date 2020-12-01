# Link: https://www.geeksforgeeks.org/largest-sum-zig-zag-sequence-in-a-matrix/
# Memoization based Python3 program to find the largest 
# sum zigzag sequence 
MAX = 100; 

dp = [[0 for i in range(MAX)] for j in range(MAX)] 

# Returns largest sum of a Zigzag sequence starting 
# from (i, j) and ending at a bottom cell. 
def largestZigZagSumRec(mat, i, j, n): 
	if (dp[i][j] != -1): 
		return dp[i][j]; 

	# If we have reached bottom 
	if (i == n - 1): 
		dp[i][j] = mat[i][j]; 
		return (dp[i][j]); 

	# Find the largest sum by considering all 
	# possible next elements in sequence. 
	zzs = 0; 
	for k in range(n): 
		if (k != j): 
			zzs = max(zzs, largestZigZagSumRec(mat, 
					i + 1, k, n)); 
	dp[i][j] = (zzs + mat[i][j]); 
	return (dp[i][j]); 

# Returns largest possible sum of a Zizag sequence 
# starting from top and ending at bottom. 
def largestZigZag(mat, n): 
	for i in range(MAX): 
		for k in range(MAX): 
			dp[i][k] = -1; 

	# Consider all cells of top row as starting point 
	res = 0; 
	for j in range(n): 
		res = max(res, largestZigZagSumRec(mat, 0, j, n)); 

	return res; 

# Driver code 
if __name__ == '__main__': 
	n = 3; 
	mat = [[4, 2, 1], [3, 9, 6], [11, 3, 15]]; 
	print("Largest zigzag sum: ", largestZigZag(mat, n)); 
