# Link: https://www.geeksforgeeks.org/delete-an-element-from-array-using-two-traversals-and-one-traversal/
# https://practice.geeksforgeeks.org/problems/rotate-and-delete/0
# https://www.geeksforgeeks.org/array-rotation/
# python program to remove a given element from an array 
# This function removes an element x from arr[] and 
# returns new size after removal. 
# Returned size is n-1 when element is present. 
# Otherwise 0 is returned to indicate failure. 
def deleteElement(arr,n,x): 

	# If x is last element, nothing to do 
	if arr[n-1]==x: 
		return n-1

	# Start from rightmost element and keep moving 
# elements one position ahead. 

	prev = arr[n-1] 
	for i in range(n-2,1,-1): 
		if arr[i]!=x: 
			curr = arr[i] 
			arr[i] = prev 
			prev = curr 

	# If element was not found 
	if i<0: 
		return 0

	# Else move the next element in place of x 
	arr[i] = prev 
	return n-1


# Driver code 
arr = [11,15,6,8,9,10] 
n = len(arr) 
x = 6
n = deleteElement(arr,n,x) 
print("Modified array is") 
for i in range(n): 
	print(arr[i],end=" ") 
