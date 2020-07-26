# Link: 
# IsDone: 0

def function(n):
	count = 0
	if n <= 0:
		return
	for i in range(1, n):
		for j in range(1, n):
			count = count + 1
	function(n - 3)
	print (count)

function(20)


