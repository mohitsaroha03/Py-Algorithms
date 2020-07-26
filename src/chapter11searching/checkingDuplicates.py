#

from collections import defaultdict
##Explain the logic
def checkDuplicates(A):
	c = 0
	# If array length is 0 or not valid
	if (len(A)==0):
		return False
	for i in range(len(A)):
		for j in range(i+1, len(A)):
			c += 1
			if (A[i] == A[j]):
				print c
				return True
	print c
	return False
 
def checkDuplicates2(A):
	c = 0
	# If array length is 0 or not valid
	if (len(A)==0):
		return False
	for i in range(len(A)):
		for j in range(0, len(A)):
			c += 1
			if (i ==j):
				continue
			if (A[i] == A[j]):
				print c
				return True
	print c
	return False
 
def checkDuplicates3(A):
	c = 0
	# If array length is 0 or not valid
	if (len(A)==0):
		return False
 
	# Sorting the array elements
	A.sort()
	for i in range(len(A)):
		c += 1
		if (A[i] == A[i+1]):
			print c
			return True
	print c
	return False
 
def checkDuplicates4(A):
	h = defaultdict(int) # default value of int is 0
	for element in A:
		if (h[element] == 1):
			print h.items()
			return True
		else:
			h[element] = 1
	return False
 
def checkDuplicates5(A):
	# Error checks
	minimum = min(A)
	maximum = max(A)
	if minimum < 0 or maximum >= len(A):
		print("Not a avalid input")
		return False
	for i in range(len(A)):
		if(A[abs(A[i])] < 0):
			return True
		else:
			A[abs(A[i])] = -A[abs(A[i])]
 
	print("No duplicates in given array.")
	return False
 
#print checkDuplicates5([1,2,3,4,5,6,7,6])
#print checkDuplicates5([0,1,2,3,4,5,6])
#print checkDuplicates5([3,2,1,2,2,3])
print checkDuplicates5([3,2,1,2,2,-3])
 
