# isGFG: , Link: 
# IsDone: 0
class DisjointSet:   
	def __init__(self, n):
		self.MAKESETUNIONBYSIZE(n)

	def MAKESET(self, n):
		self.S = [x for x in range(n)]	

	def MAKESETUNIONBYSIZE(self, n):
		self.S = [-1 for x in range(n)]	
 
	def FIND(self, X):
		if(not (X >= 0 and X < len(self.S))):
			return

		if(self.S[X] == X): 
			return X

		else:	
			return self.FIND([X])
			
	def FINDBYSIZE(self, X):
		if(self.S[X] < 0): 
			return X
		else:	
			return self.FINDBYSIZE(self.S[X])

	def UNION(self, root1, root2):
		if self.FIND(root1) == self.FIND(root2):
			return
		if(not ((root1 >= 0 and root1 < size) and (root2 >= 0 and root2 < size))):
			return	    
		self.S[root1] = root2
 
 	def UNIONBYSIZE(self, root1, root2):
		if self.FIND(root1) == self.FIND(root2) and self.FIND(root1) == -1:
			return
		if(self.S[root2] < self.S[root1]):
			self.S[root2] += self.S[root1]	    
			self.S[root1] = root2
		else:
			self.S[root1] += self.S[root2]
			self.S[root2] = root1			
 
  	def UNIONBYHEIGHT(self, root1, root2):
		if self.FIND(root1) == self.FIND(root2) and self.FIND(root1) == -1:
			return		
		if(self.S[root2] < self.S[root1]):
			self.S[root1] = root2
		elif self.S[root2] == self.S[root1] :
			self.S[root1] -= 1
		self.S[root2] = root1
			
	def printSet(self):
		print self.S
#---------------------------------------------------------------
 
if __name__ == '__main__':
    # Part a)
    uf = DisjointSet(9)
    uf.UNIONBYSIZE(1, 2)
    uf.UNIONBYSIZE(3, 4)
    uf.UNIONBYSIZE(5, 6)
    uf.printSet()

    uf.UNIONBYSIZE(1, 3)
    uf.printSet()
 
    print uf.FINDBYSIZE(2)
    uf.printSet()
    
    uf = DisjointSet(9)
    uf.UNIONBYHEIGHT(1, 2)
    uf.UNIONBYHEIGHT(3, 4)
    uf.UNIONBYHEIGHT(5, 6)
    uf.printSet()

    uf.UNIONBYHEIGHT(1, 3)    
    uf.UNIONBYHEIGHT(1, 5)
    uf.printSet()
 
    print uf.FINDBYSIZE(2)
    uf.printSet()    
