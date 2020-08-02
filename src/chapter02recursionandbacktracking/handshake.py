# Link: https://www.geeksforgeeks.org/number-of-handshakes-such-that-a-person-shakes-hands-only-once/
# link: https://www.geeksforgeeks.org/find-maximum-number-handshakes/
# IsDone: 1
# Recursive Python program 
# to count total number of 
# handshakes when a person 
# can shake hand with only one. 

# function to find all 
# possible handshakes 
def handshake(n): 

	# when n becomes 0 that means 
	# all the persons have done 
	# handshake with other 

	# def maxHandshake(n): 
	# using formula link: https://www.youtube.com/watch?v=dIejOnMP20c
	# 	return int((n * (n - 1)) / 2) 
	# n = 9
	# print(maxHandshake(n)) 

	if (n == 0): 
		return 0
	else: 
		return (n - 1) + handshake(n - 1) 

# Driver Code 
n = 9
print(handshake(n)) 
