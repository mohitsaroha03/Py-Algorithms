# Link: https://www.geeksforgeeks.org/minimum-cost-to-reverse-edges-such-that-there-is-path-between-every-pair-of-nodes/
# IsDone: 0
# Python code to find the minimum cost to 
# reverse the edges 

# Function to calculate min cost for 
# reversing the edges 
def minCost(graph, n): 

	cost1, cost2 = 0, 0; 
	
	# bool array to mark start and 
	# end node of a graph 
	start = [False]*(n + 1); 
	end = [False]*(n + 1); 

	for i in range(n): 
		a = graph[i][0]; 
		b = graph[i][1]; 
		c = graph[i][2]; 

		# This edge must start from b 
		# and end at a 
		if (start[a] or end[b]): 
			cost2 += c; 
			start[b] = True; 
			end[a] = True; 

		# This edge must start from a 
		# and end at b 
		else: 
			cost1 += c; 
			start[a] = True; 
			end[b] = True; 

	# Return minimum of both posibilities 
	return min(cost1, cost2); 

# Driver code 
if __name__ == '__main__': 
	n = 5; 
	
	# Adjacency list representation 
	# of a graph 
	graph = [[ 1, 2, 7 ], 
					[ 5, 1, 8 ], 
					[ 5, 4, 5 ], 
					[ 3, 4, 1 ], 
					[ 3, 2, 10 ]]; 

	ans = minCost(graph, n); 
	print(ans); 