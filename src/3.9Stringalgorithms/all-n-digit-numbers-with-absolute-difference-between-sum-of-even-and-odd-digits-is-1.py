# Link: https://www.geeksforgeeks.org/print-all-n-digit-numbers-with-absolute-difference-between-sum-of-even-and-odd-digits-is-1/
# IsDone: 0
# Python 3 recursive program to print all N-digit 
# numbers with absolute difference between sum of 
# even and odd digits is 1 

# Recursive function to print all N-digit numbers 
# with absolute difference between sum of even and 
# odd digits is 1. This function considers leading 
# zero as a digit 

# n --> value of input 
# out --> output array 
# index --> index of next digit to be filled 
#		 in output array 
# evenSum, oddSum --> sum of even and odd 
#					 digits so far 
def findNDigitNumsUtil(n, out, index, 
					evenSum, oddSum): 

	# Base case 
	if (index > n): 
		return

	# If number becomes n-digit 
	if (index == n): 
	
		# if absolute difference between sum of even 
		# and odd digits is 1, print the number 
		if (abs(evenSum - oddSum) == 1): 
			out[index] = '' 
			out = ''.join(out) 
			print(out, end = " ") 
		return

	# If current index is odd, then add it 
	# to odd sum and recurse 
	if (index & 1): 
		for i in range(10): 
			out[index] = chr(i + ord('0')) 
			findNDigitNumsUtil(n, out, index + 1, 
							evenSum, oddSum + i) 
								
	else: # else add to even sum and recurse 
		for i in range(10): 
			out[index] = chr(i + ord('0')) 
			findNDigitNumsUtil(n, out, index + 1, 
							evenSum + i, oddSum) 

# This is mainly a wrapper over findNDigitNumsUtil. 
# It explicitly handles leading digit and calls 
# findNDigitNumsUtil() for remaining indexes. 
def findNDigitNums(n): 

	# output array to store n-digit numbers 
	out = [0] * (n + 1) 

	# Initialize number index considered 
	# so far 
	index = 0

	# Initialize even and odd sums 
	evenSum = 0
	oddSum = 0

	# Explicitly handle first digit and call 
	# recursive function findNDigitNumsUtil 
	# for remaining indexes. Note that the 
	# first digit is considered to be present 
	# in even position. 
	for i in range(1, 10): 
		out[index] = chr(i + ord('0')) 
		findNDigitNumsUtil(n, out, index + 1, 
						evenSum + i, oddSum) 

# Driver Code 
if __name__ == "__main__": 
	
	n = 3
	findNDigitNums(n) 
