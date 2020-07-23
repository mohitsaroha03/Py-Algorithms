# isGFG: , Link: 
# IsDone: 0
def maxIndexDiff(A):
	n = len(A)
	LeftMins = [0] * (n)
	RightMaxs = [0] * (n)
	LeftMins[0] = A[0]
	for i in range(1, n):
		LeftMins[i] = min(A[i], LeftMins[i - 1])

	RightMaxs[n - 1] = A[n - 1]
	for j in range(n - 2, -1, -1):
		RightMaxs[j] = max(A[j], RightMaxs[j + 1])

	i = 0; j = 0; maxDiff = -1;
	while (j < n and i < n):
		if (LeftMins[i] < RightMaxs[j]):
			maxDiff = max(maxDiff, j - i)
			j = j + 1
		else:
			i = i + 1
	return maxDiff

A = [34, 8, 10, 3, 2, 80, 30, 33, 1]
print maxIndexDiff(A)
