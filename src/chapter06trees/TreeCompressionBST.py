''

import sys
def TreeCompression(root, previousNodeData):
	if(not root): 
		return None
	TreeCompression(root.left, previousNode)  
	if(previousNodeData == -sys.maxint):
		previousNodeData = root.data
		free(root)

	if(previousNodeData != -sys.maxint):  # Process current node
		root.data2 = previousNodeData
	return TreeCompression(root.right, previousNode)

