# isGFG: , Link: 
# IsDone: 0
def trimBST(root, minVal, maxVal): 
	if not root: 
		return 
	root.setLeft(trimBST(root.getLeft(), minVal, maxVal)) 
	root.setRight(trimBST(root.getRight(), minVal, maxVal)) 
	if minVal <= root.get_data() <= maxVal: 
		return root 
	if root.get_data() < minVal: 
		return root.getRight() 
	if root.get_data() > maxVal: 
		return root.getLeft()
		
