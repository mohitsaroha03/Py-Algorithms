# isGFG: , Link: 
# IsDone: 0

def function(n):
	count = 0
	for i in range(n / 2, n):  # Outer loop execute n/2 times
		j = 1
		count = count + 1
		while j + n / 2 <= n:  # Middle loop has break
			break
			j = j * 2
			count = count + 1

	print (count)

function(20)

