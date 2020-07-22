''

def DetectCycle(G) :
	for i in range(0, G.numVertices):
		Visited[s] = 0
		Predecessor[i] = 0
	
	for i in range(0, G.numVertices):
		if(not Visited[i] and HasCycle(G, i)):
			return 1
	return False

def HasCycle(G, u) :
	Visited[u] = 1
	for i in range(0, G.numVertices):
		if(G.adjMatrix[s][i]) :
			if(Predecessor[i] != u and Visited[i]):
				return 1
			else:
				Predecessor[i] = u
				return  HasCycle(G, i)
	return 0

