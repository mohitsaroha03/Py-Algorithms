# isGFG: , Link: 
# IsDone: 0
def moveSpacesToBegin(A):
     i = len(A) - 1
     datalist = list(A)
     j = i
     for j in range(i, -1, -1):
          if(not datalist[j].isspace()):
		temp = datalist[i]
		datalist[i] = datalist[j]
		datalist[j] = temp
		i -= 1
     A = ''.join(datalist)
     return A
A = "move these spaces to beginning"
print A, "\n", moveSpacesToBegin(A)

def moveSpacesToBegin2(A):
	n = len(A) - 1
	datalist = list(A)
	count = i = n
	for j in range(i, 0, -1):
		if(not datalist[j].isspace()):
			datalist[count] = datalist[j]
			count -= 1
			
	while(count >= 0):
		datalist[count] = ' '
		count -= 1
	A = ''.join(datalist)
	return A
A = "move these spaces to beginning"
print A, "\n", moveSpacesToBegin2(A)

