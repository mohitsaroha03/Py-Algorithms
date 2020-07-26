# Link: 
# IsDone: 0
def BinarySearchIterative(numbersList, value):
    low = 0
    high = len(numbersList) - 1
    while low <= high: 
        mid = (low + high) // 2
        if numbersList[mid] > value: high = mid - 1
        elif numbersList[mid] < value: low = mid + 1
        else: return mid
    return -1
	
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(BinarySearchIterative(A, 277))
