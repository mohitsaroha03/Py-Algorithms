# isGFG: , Link: 
# IsDone: 0
def LargestTasks(Start, n, Finish):
	sort Finish[]
	rearrange Start[] to match
	count = 1
	X[count] = 1
	for i in range(2, n):
		if(Start[i] > Finish[X[count]]):
			count = count + 1
			X[count] = I
	return X[1:count]
