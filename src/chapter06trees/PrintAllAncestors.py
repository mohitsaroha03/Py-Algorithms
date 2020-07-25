# Link: https://www.geeksforgeeks.org/print-ancestors-of-a-given-node-in-binary-tree/
# IsDone: 1

# Python program to print ancestors of given node in 
# binary tree 

# A Binary Tree node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# If target is present in tree, then prints the ancestors 
# and returns true, otherwise returns false 
def printAncestors(root, target): 
	
	# Base case 
	if root == None: 
		return False
	
	if root.data == target: 
		return True

	# If target is present in either left or right subtree 
	# of this node, then print this node 
	if (printAncestors(root.left, target) or
		printAncestors(root.right, target)): 
		print root.data, 
		return True

	# Else return False 
	return False


#          1
# 	   2    3
# 	4    5
# 7 
# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.left.left = Node(7) 

printAncestors(root, 2) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

