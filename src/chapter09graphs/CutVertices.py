''

import math
adjMatrix = [[0 for x in G.numVertices] for x in G.numVertices]
dfsnum = [0] * G.numVertices
num = 0
low = [0] * G.numVertices
def CutVertices(G, u) :
	low[u] = num
	dfsnum[u] = num
	num = num + 1
	for v in range(0, G.numVertices):
		if(G.adjMatrix[u][v] and dfsnum[v] == -1):
			CutVertices(v) 
			if(low[v] > dfsnum[u]):
				print "Cut Vetex:", u
			low[u] = min (low[u] , low[v]) 
		 
		else:  # (u,v) is a back edge
			low[u ] = min(low[u] , dfsnum[v])
