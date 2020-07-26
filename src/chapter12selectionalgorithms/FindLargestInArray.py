# Link: 
# IsDone: 0
def FindLargestInArray(A):
    max = 0
    for number in A:
        if number > max:
            max = number
    return max
	
print(FindLargestInArray([2, 1, 5, 234, 3, 44, 7, 6, 4, 5, 9, 11, 12, 14, 13]))
