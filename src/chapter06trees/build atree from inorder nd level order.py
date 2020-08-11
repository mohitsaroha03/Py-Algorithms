# Link: https://www.techiedelight.com/construct-binary-tree-from-inorder-level-order-traversals/
# Data structure to store a Binary Tree node
class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


# Recursive function to perform inorder traversal of a binary tree
def inorderTraversal(root):

	if root is None:
		return

	inorderTraversal(root.left)
	print(root.data,)
	inorderTraversal(root.right)


# Recursive function to construct a binary tree from in-order and
# level-order traversals
def buildTree(inorder, start, end, dict):

	# base case
	if start > end:
		return None

	# find the index of root node in inorder to determine the
	# boundary of left and right subtree
	index = start
	for j in range(start + 1, end + 1):
		# find node with minimum index in level order traversal
		# That would be the root node of inorder[start, end]
		if dict.get(inorder[j]) < dict.get(inorder[index]):
			index = j

	# construct the root node
	root = Node(inorder[index])

	# recursively construct the left subtree
	root.left = buildTree(inorder, start, index - 1, dict)

	# recursively construct the right subtree
	root.right = buildTree(inorder, index + 1, end, dict)

	# return root node
	return root


# Construct a binary tree from in-order and level-order traversals
def buildBT(inorder, level):

	# create a dictionary to efficiently find index of an element in
	# level-order sequence
	dict = {}
	for i, e in enumerate(level):
		dict[e] = i

	# Construct the tree and return it
	return buildTree(inorder, 0, len(inorder) - 1, dict)


if __name__ == '__main__':

	inorder = [4, 2, 5, 1, 6, 3, 7]
	level = [1, 2, 3, 4, 5, 6, 7]

	root = buildBT(inorder, level)

	print("Inorder traversal of the constructed tree: ", end='')
	inorderTraversal(root)
