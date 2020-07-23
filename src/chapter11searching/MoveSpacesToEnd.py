# isGFG: , Link: 
# IsDone: 0
def moveSpacesToEnd(A):
	n = len(A) - 1
	datalist = list(A)
	count = i = 0
	for i in range(i, n):
		if(not datalist[i].isspace()):
			datalist[count] = datalist[i]
			count += 1
			
	while(count <= n):
		datalist[count] = ' '
		count += 1
	A = ''.join(datalist)
	return A
A = "move these spaces to beginning"
print A, "\n", moveSpacesToEnd(A)

