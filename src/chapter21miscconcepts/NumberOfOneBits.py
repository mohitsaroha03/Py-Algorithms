# isGFG: , Link: 
# IsDone: 0
def number_of_ones1(n):
	count = 0
	while(n):
        count += n & 1
	    n >>= 1
	print count

def number_of_ones2(n):
	count = 0
	while(n):
	    if(n % 2 == 1):
		  	count += 1
		  	n = n / 2
	print count
	

def number_of_ones3(n):
	count = 0
	while(n):
		count += 1
		n &= n - 1
	print count

def number_of_ones4(n):
	Table = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
	count = 0
	while (n):
		count = count + Table[n & 0xF]
		n >>= 4
	print count

	

n = 11
number_of_ones1(n)
number_of_ones2(n)
number_of_ones3(n)
number_of_ones4(n)
