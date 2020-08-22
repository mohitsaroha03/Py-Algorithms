#

def majority1(A):
	n = len(A)
	for element in A:
		count = 0
		for e in A:
			if (element == e):
				count += 1
		if (count > n//2):
			return element
def majority2(A):
	A.sort()
	max_count = 1
	majority_element = A[0]
	count = 1
	element = A[0]
	for i in range(1, len(A)):
		if A[i] == element:
			count += 1
		else:
			if count > max_count:
				max_count = count
				majority_element = element
			count = 1
			element = A[i]
def majority3(A):
	A.sort()
	max_count = 1
	for i in range(len(A)-1):
		if A[i] == A[i+1]:
			max_count += 1
		else:
			max_count = 1
		if max_count > len(A)//2:
			return A[i], max_count

def majority4(A):
	A.sort()
	n = len(A)
	return A[n//2]

def majority5(A):
	count = 0
	element = -1
	n = len(A)
	for i in range(0, n - 1):
		if(count == 0):
			element = A[i]
			count = 1
		elif(element == A[i]):
			count += 1
		else:
			count -= 1
	return element, count

print majority5([1,2,3])
#print majority5([3,2,1,3,1,3,3,3,4,4,4,4])
#print majority5([3,2,1,3,1,3,3,3])
#print majority5([3,2,3,3,1,3,3,3,4,4,4,4,4])
