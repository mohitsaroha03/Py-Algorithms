# Link: https://www.geeksforgeeks.org/connect-nodes-at-same-level/
# IsDone: 1
# Python3 program to connect nodes at same 
# level using extended pre-order traversal 

class newnode: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = self.nextRight = None
		
# Sets the nextRight of root and calls 
# connectRecur() for other nodes 
def connect (p): 
	
	# This approach works only for Complete Binary Trees. 
	# In this method we set nextRight in Pre Order fashion 
	# to make sure that the nextRight of parent is set before its children. 
	# When we are at node p, we set the nextRight of its left and right children. 
	# Since the tree is complete tree, nextRight of p’s left child (p->left->nextRight) 
	# will always be p’s right child, and nextRight of p’s right child (p->right->nextRight) 
	# will always be left child of p’s nextRight (if p is not the rightmost node at its level). 
	# If p is the rightmost node, then nextRight of p’s right child will be NULL.
	
	
	# Set the nextRight for root 
	p.nextRight = None

	# Set the next right for rest of 
	# the nodes (other than root) 
	connectRecur(p) 

# Set next right of all descendents of p. 
# Assumption: p is a compete binary tree 
def connectRecur(p): 
	
	# Base case 
	if (not p): 
		return
	
	# Set the nextRight pointer for p's 
	# left child 
	if (p.left): 
		p.left.nextRight = p.right 
	
	# Set the nextRight pointer for p's right 
	# child p.nextRight will be None if p is 
	# the right most child at its level 
	if (p.right): 
		if p.nextRight: 
			p.right.nextRight = p.nextRight.left 
		else: 
			p.right.nextRight = None
	
	# Set nextRight for other nodes in 
	# pre order fashion 
	connectRecur(p.left) 
	connectRecur(p.right) 

# Driver Code 
if __name__ == '__main__': 

	# Constructed binary tree is 
	#    10 
	#	 / \ 
	#  8	 2 
	# / 
	# 3 
	root = newnode(10) 
	root.left = newnode(8) 
	root.right = newnode(2) 
	root.left.left = newnode(3) 

	# Populates nextRight pointer in all nodes 
	connect(root) 

	# Let us check the values of nextRight pointers 
	print "Following are populated nextRight", "pointers in the tree (-1 is printed", "if there is no nextRight" 
	print "nextRight of", root.data, "is " 
	if root.nextRight: 
		print(root.nextRight.data) 
	else: 
		print(-1) 
	print "nextRight of", root.left.data, "is " 
	if root.left.nextRight: 
		print(root.left.nextRight.data) 
	else: 
		print(-1) 
	print "nextRight of", root.right.data, "is " 
	if root.right.nextRight: 
		print(root.right.nextRight.data) 
	else: 
		print(-1) 
	print "nextRight of", root.left.left.data, "is " 
	if root.left.left.nextRight: 
		print(root.left.left.nextRight.data) 
	else: 
		print(-1) 
