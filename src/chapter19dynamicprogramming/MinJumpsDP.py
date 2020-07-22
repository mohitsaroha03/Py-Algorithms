''

import sys
def minJumps(A):
	n = len(A)
	jumps = [0] * (n)
	if (n == 0 or A[0] == 0):
		return sys.maxint + 1

	jumps[0] = 0
	for i in range(1, n):
		jumps[i] = sys.maxint + 1
		for j in range(0, i):
			if (i <= j + A[j] and jumps[j] != sys.maxint + 1):
				jumps[i] = min(jumps[i], jumps[j] + 1)
				break
	return jumps[n - 1]

A = [1, 3, 6, 1, 0, 9]
print "Minimum number of jumps to reach end is ", minJumps(A)

A = [2, 3, 1, 1, 4]
print "Minimum number of jumps to reach end is ", minJumps(A)
