# isGFG: , Link: 
# IsDone: 0
def PrintAllAncestors(root, node):
	if(root == NULL):
		return 0
	if(root.left == node or root.right == node or  PrintAllAncestors(root.left, node) or PrintAllAncestors(root.right, node)):
		print(root.data)
		return 1
	return 0
