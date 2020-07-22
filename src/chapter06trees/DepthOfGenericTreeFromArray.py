''

def findDepthInGenericTree(P):
	maxDepth = -1
	currentDepth = -1
	for i in range (0, len(P)):
		currentDepth = 0
		j = i
		while(P[j] != -1):
		       currentDepth += 1
		       j = P[j]
		if(currentDepth > maxDepth):
			maxDepth = currentDepth
	
	return maxDepth

P = [-1, 0, 1, 6, 6, 0, 0, 2, 7]
print "Depth of given Generic Tree is:", findDepthInGenericTree(P)
