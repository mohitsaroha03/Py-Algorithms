# Link: 
# IsDone: 0

# Python3 program to remove BST keys 
# outside the given range 

# A BST node has key, and left and right 
# pointers. A utility function to create 
# a new BST node with key as given num 
class newNode: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None
		
# Removes all nodes having value outside 
# the given range and returns the root 
# of modified tree 
def removeOutsideRange(root, Min, Max): 
	
	# Base Case 
	if root == None: 
		return None
	
	# First fix the left and right 
	# subtrees of root 
	root.left = removeOutsideRange(root.left, Min, Max) 
	root.right = removeOutsideRange(root.right,	Min, Max) 
	
	# Now fix the root. There are 2 
	# possible cases for toot 
	# 1.a) Root's key is smaller than 
	#	 min value (root is not in range) 
	if root.key < Min: 
		rChild = root.right 
		return rChild 
		
	# 1.b) Root's key is greater than max 
	#	 value (root is not in range) 
	if root.key > Max: 
		lChild = root.left 
		return lChild 
		
	# 2. Root is in range 
	return root 


# A utility function to insert a given 
# key to BST 
def insert(root, key): 
	if root == None: 
		return newNode(key) 
	if root.key > key: 
		root.left = insert(root.left, key) 
	else: 
		root.right = insert(root.right, key) 
	return root 

# Utility function to traverse the binary 
# tree after conversion 
def inorderTraversal(root): 
	if root: 
		inorderTraversal( root.left) 
		print(root.key) 
		inorderTraversal( root.right) 

# Driver Code 
if __name__ == '__main__': 
	root = None
	root = insert(root, 6) 
	root = insert(root, -13) 
	root = insert(root, 14) 
	root = insert(root, -8) 
	root = insert(root, 15) 
	root = insert(root, 13) 
	root = insert(root, 7) 

	print("Inorder traversal of the given tree is:",) 
	inorderTraversal(root) 

	root = removeOutsideRange(root, -10, 13) 
	print() 
	print("Inorder traversal of the modified tree is:", ) 
	inorderTraversal(root) 