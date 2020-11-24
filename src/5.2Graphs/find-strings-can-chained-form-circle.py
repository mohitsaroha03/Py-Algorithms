# Link: https://www.geeksforgeeks.org/given-array-strings-find-strings-can-chained-form-circle/
# IsDone: 0
# Python program to check if a given directed graph is Eulerian or not 
CHARS = 26

# A class that represents an undirected graph 
class Graph(object): 
	def __init__(self, V): 
		self.V = V	 # No. of vertices 
		self.adj = [[] for x in xrange(V)] # a dynamic array 
		self.inp = [0] * V 

	# function to add an edge to graph 
	def addEdge(self, v, w): 
		self.adj[v].append(w) 
		self.inp[w]+=1

	# Method to check if this graph is Eulerian or not 
	def isSC(self): 
		# Mark all the vertices as not visited (For first DFS) 
		visited = [False] * self.V 

		# Find the first vertex with non-zero degree 
		n = 0
		for n in xrange(self.V): 
			# adj is an array(vertex) of array(other vertex from parent vertex)
			# here we are finding a vertex which has degree(in degree and out degree) more than 0
			if len(self.adj[n]) > 0: 
				break

		# Do DFS traversal starting from first non zero degree vertex. 
		self.DFSUtil(n, visited) 

		# If DFS traversal doesn't visit all vertices, then return false. 
		for i in xrange(self.V): 
			if len(self.adj[i]) > 0 and visited[i] == False: 
				return False

		# Create a reversed graph 
		gr = self.getTranspose() 

		# Mark all the vertices as not visited (For second DFS) 
		for i in xrange(self.V): 
			visited[i] = False

		# Do DFS for reversed graph starting from first vertex. 
		# Staring Vertex must be same starting point of first DFS 
		gr.DFSUtil(n, visited) 

		# If all vertices are not visited in second DFS, then 
		# return false 
		for i in xrange(self.V): 
			if len(self.adj[i]) > 0 and visited[i] == False: 
				return False

		return True

	# This function returns true if the directed graph has an eulerian 
	# cycle, otherwise returns false 
	def isEulerianCycle(self): 

		# Check if all non-zero degree vertices are connected 
		if self.isSC() == False: 
			return False

		# Check if in degree and out degree of every vertex is same 
		for i in xrange(self.V): 
			if len(self.adj[i]) != self.inp[i]: 
				return False

		return True

	# A recursive function to do DFS starting from v 
	def DFSUtil(self, v, visited): 

		# Mark the current node as visited and print it 
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex 
		for i in xrange(len(self.adj[v])): 
			if not visited[self.adj[v][i]]: 
				self.DFSUtil(self.adj[v][i], visited) 

	# Function that returns reverse (or transpose) of this graph 
	# This function is needed in isSC() 
	def getTranspose(self): 
		g = Graph(self.V) 
		for v in xrange(self.V): 
			# Recur for all the vertices adjacent to this vertex 
			for i in xrange(len(self.adj[v])): 
				g.adj[self.adj[v][i]].append(v) 
				g.inp[v]+=1
		return g 

# This function takes an of strings and returns true 
# if the given array of strings can be chained to 
# form cycle 
def canBeChained(arr, n): 

	# Create a graph with 'aplha' edges 
	g = Graph(CHARS) 

	# Create an edge from first character to last character 
	# of every string 
	for i in xrange(n): 
		s = arr[i] 
		g.addEdge(ord(s[0])-ord('a'), ord(s[len(s)-1])-ord('a')) 

	# The given array of strings can be chained if there 
	# is an eulerian cycle in the created graph 
	return g.isEulerianCycle() 

# Driver program 
arr1 = ["for", "geek", "rig", "kaf"] 
n1 = len(arr1) 
if canBeChained(arr1, n1): 
	print "Can be chained"
else: 
	print "Cant be chained"

arr2 = ["aab", "abb"] 
n2 = len(arr2) 
if canBeChained(arr2, n2): 
	print "Can be chained"
else: 
	print "Can't be chained"