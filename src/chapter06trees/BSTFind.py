# isGFG: , Link: 
# IsDone: 0
# Search the key from node, iteratively
def Find(self, root, data):
	currentNode = root
	while currentNode:
	    if data == currentNode.get_data():
		return currentNode
	    if key < currentNode.get_data():
		currentNode = currentNode.getLeft()
	    else:
		currentNode = currentNode.getRight()
	return None
