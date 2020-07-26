# Link: 
# IsDone: 0
def areStructurullySameTrees(root1, root2):
	if (not root1.left) and not (root1.right) and (not root2.left) and \
		not (root2.right) and root1.data == root2.data:
		return True

	if (root1.data != root2.data) or (root1.left and not root2.left) or \
		(not root1.left and root2.left) or (root1.right and not root2.right) \
		or (not root1.right and root2.right): 
		return False

	left = areStructurullySameTrees(root1.left, root2.left) if root1.left and root2.left else True
	right = areStructurullySameTrees(root1.right, root2.right) if root1.right and root2.right else True
	return left and right
