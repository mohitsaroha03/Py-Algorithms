# Link: https://www.geeksforgeeks.org/minimum-number-of-sub-strings-of-a-string-such-that-all-are-power-of-5/
# Python 3 implementation of the approach 

# Function that returns true 
# if n is a power of 5 
def ispower( n): 
	if (n < 125): 
		return (n == 1 or n == 5 or n == 25) 
	if (n % 125 != 0): 
		return 0
	else: 
		return ispower(n // 125) 


# Function to return the decimal 
# value of binary equivalent 
def number(s, i, j): 
	ans = 0
	for x in range( i, j) : 
		ans = ans * 2 + (ord(s[x]) - ord('0')) 
	return ans 

# Function to return the minimum cuts required 
def minCuts(s, n): 

	# Allocating memory for dp[] array 
	dp=[n+1 for i in range(n+1)] 
	dp[0] = 0; 

	# From length 1 to n 
	for i in range(1, n+1) : 

		# If previous character is '0' then ignore 
		# to avoid number with leading 0s. 
		if (s[i - 1] == '0'): 
			continue
		for j in range(i) : 

			# Ignore s[j] = '0' starting numbers 
			if (s[j] == '0'): 
				continue

			# Number formed from s[j....i] 
			num = number(s, j, i) 

			# Check for power of 5 
			if (not ispower(num)): 
				continue

			# Assigning min value to get min cut possible 
			dp[i] = min(dp[i], dp[j] + 1) 

	# (n + 1) to check if all the strings are traversed 
	# and no divisible by 5 is obtained like 000000 
	if dp[n] < n + 1: 
		return dp[n] 
	else: 
		return -1

# Driver code 
if __name__== "__main__": 
	s = "101101101"
	n = len(s) 
	print(minCuts(s, n)) 