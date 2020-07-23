# isGFG: , Link: 
# IsDone: 0
def CatalanRecursive(n):
	if n == 0:
		return 1
	else:
		count = 0
		for i in range(n):
			count += CatalanRecursive(i) * CatalanRecursive(n - 1 - i)
		return count	

print CatalanRecursive(4)
