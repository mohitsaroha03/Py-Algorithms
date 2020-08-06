# Link: https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
# Python3 program to find the 
# repeating and missing elements 
# using Maps 
def main(): 
	
	arr = [ 4, 3, 6, 2, 1, 1 ] 
	
	numberMap = {} 
	
	max = len(arr) 
	for i in arr: 
		if not i in numberMap: 
			numberMap[i] = True
			
		else: 
			print("Repeating =", i) 
	
	for i in range(1, max + 1): 
		if not i in numberMap: 
			print("Missing =", i) 
main() 
