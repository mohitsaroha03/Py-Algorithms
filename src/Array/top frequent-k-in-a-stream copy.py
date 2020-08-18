# Link: https://www.geeksforgeeks.org/find-top-k-or-most-frequent-numbers-in-a-stream/
# Python program to find top k elements in a stream 

# Function to print top k numbers 
def kTop(a, n, k): 

	# list of size k + 1 to store elements 
	top = [0 for i in range(k + 1)] 

	# dictionary to keep track of frequency 
	freq = {i:0 for i in range(k + 1)} 

	# iterate till the end of stream 
	for m in range(n): 

		# increase the frequency 
		if a[m] in freq.keys(): 
			freq[a[m]] += 1
		else: 
			freq[a[m]] = 1

		# store that element in top array 
		top[k] = a[m] 

		i = top.index(a[m]) 
		i -= 1
		
		while i >= 0: 

			# compare the frequency and swap if higher 
			# frequency element is stored next to it 
			if (freq[top[i]] < freq[top[i + 1]]): 
				t = top[i] 
				top[i] = top[i + 1] 
				top[i + 1] = t 
			
			# if frequency is same compare the elements 
			# and swap if next element is high 
			elif ((freq[top[i]] == freq[top[i + 1]]) and (top[i] > top[i + 1])): 
				t = top[i] 
				top[i] = top[i + 1] 
				top[i + 1] = t 
			else: 
				break
			i -= 1
		
		# print top k elements 
		i = 0
		while i < k and top[i] != 0: 
			print top[i], 
			i += 1
	print

# Driver program to test above function 
k = 4
arr = [ 5, 2, 1, 3, 2 ] 
n = len(arr) 
kTop(arr, n, k) 