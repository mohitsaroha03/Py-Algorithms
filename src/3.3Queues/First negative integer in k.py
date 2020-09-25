# Link: https://www.geeksforgeeks.org/first-negative-integer-every-window-size-k/
# IsDone: 1

# Python3 implementation to find the 
# first negative integer in every window 
# of size k import deque() from collections 
from collections import deque 

# function to find the first negative 
# integer in every window of size k 
def printFirstNegativeInteger(arr, n, k): 
	
	# A Double Ended Queue, Di that will store 
	# indexes of useful array elements for the 
	# current window of size k. The useful 
	# elements are all negative integers. 
	Di = deque() 

	# Process first k (or first window) 
	# elements of array 
	for i in range(k): 
		
		# Add current element at the rear of Di 
		# if it is a negative integer 
		if (arr[i] < 0): 
			Di.append(i); 
	
	# Process rest of the elements, i.e., 
	# from arr[k] to arr[n-1] 
	for i in range(k, n): 
		
		# if the window does not have 
		# a negative integer 
		if (not Di): 
			print(0) 
		
		# if Di is not empty then the element 
		# at the front of the queue is the first 
		# negative integer of the previous window 
		else: 
			print(arr[Di[0]]); 

		# Remove the elements which are 
		# out of this window 
		while Di and Di[0] <= (i - k): 
			Di.popleft() # Remove from front of queue 

		# Add current element at the rear of Di 
		# if it is a negative integer 
		if (arr[i] < 0): 
			Di.append(i); 

	# Print the first negative 
	# integer of last window 
	if not Di: 
		print(0) 
	else: 
		print(arr[Di[0]]) 

def printFirstNegativeInteger1(arr, k): 
	firstNegativeIndex = 0

	for i in range(k - 1, len(arr)): 

		# skip out of window and positive elements 
		while firstNegativeIndex < i and (firstNegativeIndex <= i - k or arr[firstNegativeIndex] > 0): 
			firstNegativeIndex += 1

		# check if a negative element is found, otherwise use 0 
		firstNegativeElement = arr[firstNegativeIndex] if arr[firstNegativeIndex] < 0 else 0
		print 'ele: ', firstNegativeElement 


if __name__ == "__main__": 
	arr = [-12, 1, 7, 8, 15, 30, 16, -28] 
	k = 3
	printFirstNegativeInteger(arr, len(arr), k) 
	# printFirstNegativeInteger1(arr, k) 

	
# Driver Code 
# if __name__ =="__main__": 
# 	arr = [12, -1, -7, 8, -15, 30, 16, 28] 
# 	n = len(arr) 
# 	k = 3
# 	printFirstNegativeInteger(arr, n, k); 