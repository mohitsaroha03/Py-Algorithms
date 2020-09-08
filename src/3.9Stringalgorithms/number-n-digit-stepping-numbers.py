# Link: https://www.geeksforgeeks.org/number-n-digit-stepping-numbers/
# IsDone: 0
# Python3 program to calculate 
# the number of n digit 
# stepping numbers. 

# function that calculates 
# the answer 
def answer(n): 
	
	# dp[i][j] stores count of 
	# i digit stepping numbers 
	# ending with digit j. 
	dp = [[0 for x in range(10)] 
			for y in range(n + 1)]; 

	# if n is 1 then answer 
	# will be 10. 
	if (n == 1): 
		return 10; 
	for j in range(10): 
		dp[1][j] = 1; 

	# Compute values for count 
	# of digits more than 1. 
	for i in range(2, n + 1): 
		for j in range(10): 
			
			# If ending digit is 0 
			if (j == 0): 
				dp[i][j] = dp[i - 1][j + 1]; 
				
			# If ending digit is 9 
			elif (j == 9): 
				dp[i][j] = dp[i - 1][j - 1]; 
				
			# For other digits. 
			else: 
				dp[i][j] = (dp[i - 1][j - 1] +
							dp[i - 1][j + 1]); 
				
	# stores the final answer 
	sum = 0; 
	for j in range(1, 10): 
		sum = sum + dp[n][j]; 
	return sum; 

# Driver Code 
n = 2; 
print(answer(n)); 
