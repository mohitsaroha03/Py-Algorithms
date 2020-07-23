# isGFG: , Link: 
# IsDone: 0
def FirstRepeatedChar (str):
	size = len(str)
	count = [0] * (256)
	for i in range(size):
		if(count[ord(str[i])] == 1):
			print  str[i]
			break
		else:    
			count[ord(str[i])] += 1
	if(i == size):
		print "No Repeated Characters"
	return 0

FirstRepeatedChar(['C', 'a', 'r', 'e', 'e', 'r', 'm', 'o', 'n', 'k'])
