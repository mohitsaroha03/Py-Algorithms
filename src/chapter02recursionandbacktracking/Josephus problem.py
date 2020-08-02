# Link: https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
# https://www.geeksforgeeks.org/josephus-problem-iterative-solution/
# https://www.geeksforgeeks.org/josephus-problem-set-2-simple-solution-k-2/
# solution: https://www.youtube.com/watch?v=uCsD3ZGzMgE
#  make n as 2^a + l so survivor will be 2l + 1 
# IsDone: 1
# Python code for Josephus Problem 

def josephus(n, k): 

	if (n == 1): 
		return 1
	else: 
	
	
		# The position returned by 
		# josephus(n - 1, k) is adjusted 
		# because the recursive call 
		# josephus(n - 1, k) considers 
		# the original position 
		# k%n + 1 as position 1 
		return (josephus(n - 1, k) + k-1) % n + 1

# Driver Program to test above function 

n = 6
k = 2

print("The chosen place is ", josephus(n, k)) 