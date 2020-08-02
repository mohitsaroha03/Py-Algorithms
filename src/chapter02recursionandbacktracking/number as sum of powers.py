# Link: https://www.geeksforgeeks.org/count-ways-express-number-sum-powers/
# IsDone: 1
# Python program to count number of ways 
# to express x as sum of n-th power 
# of unique natural numbers. 

# num is current num. 
def countWaysUtil(x,n,num): 

	# Base cases 
	val = (x - pow(num, n)) 
	if (val == 0): 
		return 1
	if (val < 0): 
		return 0

	# Consider two possibilities, num is 
	# included and num is not included. 
	l = countWaysUtil(val, n, num + 1)
	r = countWaysUtil(x, n, num + 1) 
	return l + r


# Returns number of ways to express 
# x as sum of n-th power of two. 
def countWays(x,n): 
	return countWaysUtil(x, n, 1) 

	
# Driver code 
x = 8
n = 2

print(countWays(x, n)) 
