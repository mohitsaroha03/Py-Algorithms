# isGFG: , Link: 
# IsDone: 0
def fillNextSiblings(root):
	if (root == None): 
		return

	if root.left: 
		root.left.nextSibling = root.right

	if roo.tright:
		if root.nextSibling:
			root.right.nextSibling = root.nextSibling.left 
		else:
			root.right.nextSibling = None

	fillNextSiblings(root.left)
	fillNextSiblings(root.right)
