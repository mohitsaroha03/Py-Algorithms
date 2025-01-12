# Link: https://www.geeksforgeeks.org/print-left-view-binary-tree/
# IsDone: 1
# Python program to print left view of Binary Tree 

# A binary tree node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


# Recursive function pritn left view of a binary tree 
def leftViewUtil(root, level, max_level): 
	
	# Base Case 
	if root is None: 
		return

	# If this is the first node of its level 
	if (max_level[0] < level): 
		print "% d\t" %(root.data), 
		max_level[0] = level 

	# Recur for left and right subtree 
	leftViewUtil(root.left, level + 1, max_level) 
	leftViewUtil(root.right, level + 1, max_level) 


# A wrapper over leftViewUtil() 
def leftView(root): 
	max_level = [0] 
	leftViewUtil(root, 1, max_level) 


# Driver program to test above function 
root = Node(12) 
root.left = Node(10) 
root.right = Node(20) 
root.right.left = Node(25) 
root.right.right = Node(40) 

leftView(root) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
