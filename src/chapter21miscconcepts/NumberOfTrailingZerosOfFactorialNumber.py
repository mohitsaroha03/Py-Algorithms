''

def number_of_trailing_zeros_of_factorial_number(n):
	count = 0
	if(n < 0):  
		return -1
	i = 5
	while n / i > 0:
		count += n / i
		i *= 5
	return count

print number_of_trailing_zeros_of_factorial_number(100)
