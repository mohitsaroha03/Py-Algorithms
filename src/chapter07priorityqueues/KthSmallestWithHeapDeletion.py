# isGFG: , Link: 
# IsDone: 0
def kthSmallest(collection, k):
    """Return kth smallest element in collection for valid k >=1 """
    A = collection[:k]
    buildHeap(A)
    for i in range(k, len(collection)):
        if collection[i] < A[0]:
            A[0] = collection[i]
            heapify(A, 0, k)
    return A[0]

def buildHeap(A):
    n = len(A)
    for i in range(n / 2 - 1, -1, -1):
        heapify(A, i, n)

def heapify (A, index, maxIndex):
    """Ensure structure rooted at A[index] is a heap"""
    left = 2 * index + 1
    right = 2 * index + 2
    if left < maxIndex and A[left] > A[index]:
        largest = left
    else: 
        largest = index
    if right < maxIndex and A[right] > A[largest]:
        largest = right

    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        heapify(A, largest, maxIndex)

print kthSmallest(range(10), 3)
print kthSmallest(range(10), 1)
print kthSmallest(range(10), 10)
