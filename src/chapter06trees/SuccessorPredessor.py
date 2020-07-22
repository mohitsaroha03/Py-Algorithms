''

# Successror of a node in BST
def successorBST(root):
	temp = None
	if root.getRight():
	    temp = root.getRight()
	    while temp.getLeft():
		temp = s.getLeft()
	return temp

# Predecessor of a node in BST
def predecessorBST(root):
	temp = None
	if root.getLeft():
	    temp = root.getLeft()
	    while temp.getRight():
		temp = temp.getRight()
	return temp
