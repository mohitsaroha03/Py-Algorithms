# Link: https://www.geeksforgeeks.org/longest-repeating-subsequence/
# Python 3 program to find the longest repeating
# subsequence using recursion

dp = [[0 for i in range(1000)] for j in range(1000)]

# This function mainly returns LCS(str, str) 
# with a condition that same characters at 
# same index are not considered. 

def findLongestRepeatingSubSeq( X, m, n):
	
	if(dp[m][n]!=-1):
		return dp[m][n]
	
	# return if we have reached the end of either string
	if (m == 0 or n == 0):
		dp[m][n] = 0
		return dp[m][n]

	# if characters at index m and n matches 
	# and index is different
	if (X[m - 1] == X[n - 1] and m != n):
		dp[m][n] = findLongestRepeatingSubSeq(X, 
							m - 1, n - 1) + 1
		
		return dp[m][n]

	# else if characters at index m and n don't match
	dp[m][n] = max (findLongestRepeatingSubSeq(X, m, n - 1), 
						findLongestRepeatingSubSeq(X, m - 1, n))
	return dp[m][n]

# Longest Repeated Subsequence Problem
if __name__ == "__main__":
	str = "aabb"
	m = len(str)

dp =[[-1 for i in range(1000)] for j in range(1000)]
print( "The length of the largest subsequence that"
			" repeats itself is : "
		, findLongestRepeatingSubSeq(str,m,m))