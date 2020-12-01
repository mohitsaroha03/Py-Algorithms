# Link: https://www.geeksforgeeks.org/count-strings-can-formed-using-b-c-given-constraints/
# Python 3 program to count number of strings 
# of n characters with 

# n is total number of characters. 
# bCount and cCount are counts of 'b' 
# and 'c' respectively. 
def countStrUtil(dp, n, bCount=1,cCount=2): 

	# Base cases 
	if (bCount < 0 or cCount < 0): 
		return 0
	if (n == 0): 
		return 1
	if (bCount == 0 and cCount == 0): 
		return 1

	# if we had saw this combination previously 
	if (dp[n][bCount][cCount] != -1): 
		return dp[n][bCount][cCount] 

	# Three cases, we choose, a or b or c 
	# In all three cases n decreases by 1. 
	res = countStrUtil(dp, n-1, bCount, cCount) 
	res += countStrUtil(dp, n-1, bCount-1, cCount) 
	res += countStrUtil(dp, n-1, bCount, cCount-1) 

	dp[n][bCount][cCount] = res 
	return dp[n][bCount][cCount] 

# A wrapper over countStrUtil() 
def countStr(n): 

	dp = [ [ [-1 for x in range(n+2)] for y in range(3)]for z in range(4)] 
	return countStrUtil(dp, n) 

# Driver code 
if __name__ == "__main__": 
	
	n = 3 # Total number of characters 
	print(countStr(n)) 