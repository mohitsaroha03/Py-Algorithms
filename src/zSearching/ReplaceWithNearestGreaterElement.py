# Link: 
# IsDone: 0
def replaceWithNearestGreaterElement(A):
	nextNearestGreater = float("-inf")
	i = j = 0
	for i in range(0, len(A) - 1):
		nextNearestGreater = float("-inf")
		for j in range(i + 1, len(A)):
			if A[i] < A[j]:
				nextNearestGreater = A[j]
				break
		print("For the element " + str(A[i]) + ", " + str(nextNearestGreater) + " is the nearest greater element")

replaceWithNearestGreaterElement([6, 2, 4, 1, 2, 1, 2, 2, 10])
