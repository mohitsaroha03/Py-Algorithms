''

def sortedArrayToBST(root, array):
	length = len(array)
	if length == 0: 
		return None
	if length == 1: 
		return TreeNode(array[0])
	root = BSTNode(array[length / 2])
	root.left = sortedArrayToBST(array[:length / 2])
	root.right = sortedArrayToBST(array[length / 2 + 1:])
	return root
