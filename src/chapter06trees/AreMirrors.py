# Link: 
# IsDone: 0
def AreMirrors(root1, root2):
	if(root1 == None and root2 == None): 	
		return 1
	if(root1 == None or root2 == None): 
		return 0
	if(root1.data != root2.data): 	
		return 0
	else:
		return AreMirrors(root1.left, root2.right) and AreMirrors(root1.right, root2.left)
