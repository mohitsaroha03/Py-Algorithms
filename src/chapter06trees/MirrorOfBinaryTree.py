''

def MirrorOfBinaryTree(root):
	if(root != None):
		MirrorOfBinaryTree(root.left)
		MirrorOfBinaryTree(root.right)

		# swap the pointers in this node
		temp = root.left
		root.left = root.right
		root.right = temp
	
	return root
