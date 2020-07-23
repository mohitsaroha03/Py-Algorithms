# isGFG: , Link: 
# IsDone: 0
def Knapsack(knapsackSize, itemsValue, itemsWeight):
	numItems = len(itemsValue)
	M = [[0 for x in range(knapsackSize + 1)] for x in range(len(itemsValue))]
	for i in range(1, numItems):
		for j in range(knapsackSize + 1):
			value = itemsValue[i]
			weight = itemsWeight[i]
			if weight > j:
				M[i][j] = M[i - 1][j]
			else:
				M[i][j] = max(M[i - 1][j], M[i - 1][j - weight] + value)
 
	return M[numItems - 1][knapsackSize]
	
print Knapsack(50, [60, 100, 120], [10, 20, 30])	
