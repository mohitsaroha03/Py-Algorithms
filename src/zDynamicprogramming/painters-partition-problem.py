# Link: https://www.geeksforgeeks.org/painters-partition-problem/
# A DP based Python3 program for 
# painter's partition problem 

# function to calculate sum between 
# two indices in list 
def sum(arr, start, to): 
	total = 0
	for i in range(start, to + 1): 
		total += arr[i] 
	return total 

# bottom up tabular dp 
def findMax(arr, n, k): 
	
	# initialize table 
	dp = [[0 for i in range(n + 1)] 
			for j in range(k + 1)] 

	# base cases 
	# k=1 
	for i in range(1, n + 1): 
		dp[1][i] = sum(arr, 0, i - 1) 

	# n=1 
	for i in range(1, k + 1): 
		dp[i][1] = arr[0] 

	# 2 to k partitions 
	for i in range(2, k + 1): # 2 to n boards 
		for j in range(2, n + 1): 
			
			# track minimum 
			best = 100000000
			
			# i-1 th separator before position arr[p=1..j] 
			for p in range(1, j + 1): 
				best = min(best, max(dp[i - 1][p], 
								sum(arr, p, j - 1)))	 

			dp[i][j] = best 

	# required 
	return dp[k][n] 

# Driver Code 
arr = [10, 20, 60, 50, 30, 40] 
n = len(arr) 
k = 3
print(findMax(arr, n, k)) 