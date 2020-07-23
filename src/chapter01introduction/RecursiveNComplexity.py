# isGFG: , Link: 
# IsDone: 0

count = 0
def function(n):
	global count
	count = 1
	if n <= 0:
		return
	for i in range(1, n):
		count = count + 1
	n = n // 2;
	function(n)
	print count

function(200)

def Function2(n):
	if n <= 0:
		return
	print ("*")
	Function2(n / 2)
	Function2(n / 2)
	print ("*")

function(20)
