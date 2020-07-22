''

def FindSmallestAndLargestInArray(A):
	max = 0
	min = 0
	for number in A:
		if number > max:
			max = number
		elif number < min:
			min = number

	print("Smallest: %d", min)	
	print("Largest: %d", max)	

FindSmallestAndLargestInArray([2, 1, 5, 234, 3, 44, 7, 6, 4, 5, 9, 11, 12, 14, 13])
