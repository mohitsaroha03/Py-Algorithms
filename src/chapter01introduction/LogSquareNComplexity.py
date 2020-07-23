# isGFG: , Link: 
# IsDone: 0

count = 0
def logarithms(n):
	i = 1
	global count
	while i <= n: 
		j = n
		while j > 0:
			j = j // 2
			count = count + 1
		i = i * 2
	return count
	
print(logarithms(10))
