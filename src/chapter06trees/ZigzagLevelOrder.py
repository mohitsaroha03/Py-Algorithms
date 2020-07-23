# isGFG: , Link: 
# IsDone: 0
def zigzagLevelOrder(self, root):
	result = []
	currentLevel = []
	if root != None:
	    currentLevel.append(root)
	leftToRight = True
	while len(currentLevel) > 0:
	    levelresult = []
	    nextLevel = []
	    while len(currentLevel) > 0:
		node = currentLevel.pop()
		levelresult.append(node.val)
		if leftToRight:
		    if node.left != None:
			nextLevel.append(node.left)
		    if node.right != None:
			nextLevel.append(node.right)
		else:
		    if node.right != None:
			nextLevel.append(node.right)
		    if node.left != None:
			nextLevel.append(node.left)
	    currentLevel = nextLevel
	    result.append(levelresult)
	    leftToRight = not leftToRight
	return result
