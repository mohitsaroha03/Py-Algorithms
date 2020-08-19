# Link: 
# IsDone: 0
def maxDepth(root):
	if root == None:
	    return 0
	return max(maxDepth(root.getLeft()), maxDepth(root.getRight())) + 1

def maxDepth(self, root):
	if root == None:
	    return 0
	q = []
	q.append([root, 1])
	temp = 0
	while len(q) != 0:
	    node, depth = q.pop()
	    depth = max(temp, dep)
	    if node.getLeft() != None:
		q.append([node.getLeft(), depth + 1])
	    if node.getRight() != None:
		q.append([node.getRight(), depth + 1])
	return temp
	
