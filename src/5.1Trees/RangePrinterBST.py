# Link: https://www.geeksforgeeks.org/print-bst-keys-in-the-given-range/
# IsDone: 1
# Python program to find BST keys in given range 

# A binary tree node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# The function prints all the keys in the gicven range 
# [k1..k2]. Assumes that k1 < k2 
def Print(root, min, max): 
	
	# Base Case 
	if root is None: 
		return

	# Since the desired o/p is sorted, recurse for left 
	# subtree first. If root.data is greater than min, then 
	# only we can get o/p keys in left subtree 
	if min < root.data : 
		Print(root.left, min, max) 

	# If root's data lies in range, then prints root's data 
	if min <= root.data and max >= root.data: 
		print root.data, 

	# If root.data is smaller than max, then only we can get 
	# o/p keys in right subtree 
	if max > root.data: 
		Print(root.right, min, max) 

# Driver function to test above function 
min = 10 ; max = 25 ; 
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 

Print(root, min, max) 
