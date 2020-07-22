''

# row of n coins
coins = [1, 2, 3, 4, 5]
n = len(coins)

# each time it is our turn, take the max of the two available moves (but the minimum of the opponent's two potential moves)
V = []
for i in range(n):
	V.append([0] * n)

for i in range(n):
	for j in range(n):
		if i == j:
			V[i][j] = coins[i]
		elif j == i + 1:
			V[i][j] = max(coins[i], coins[j])
		
		# only valid if i < j
		if (i + 2) <= j:
			take_start = V[i + 2][j]
		else:
			take_start = 0
		if (i + 1) <= (j - 1):
			take_end = V[i + 1][j - 1]
		else:
			take_start = 0	

