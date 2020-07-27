# Link: https://www.geeksforgeeks.org/minimum-number-of-bracket-reversals-needed-to-make-an-expression-balanced/
# IsDone: 0
# Python3 program to find minimum number of 
# reversals required to balance an expression 

# Returns count of minimum reversals 
# for making expr balanced. Returns -1 
# if expr cannot be balanced. 
def countMinReversals(expr): 

	lenn = len(expr) 

	# length of expression must be even 
	# to make it balanced by using reversals. 
	if (lenn % 2) : 
		return -1

	# After this loop, stack contains 
	# unbalanced part of expression, 
	# i.e., expression of the form "...." 
	s = [] 
	for i in range(lenn): 
		if (expr[i] =='' and len(s)): 

			if (s[0] == '') : 
				s.pop(0) 
			else: 
				s.insert(0, expr[i]) 
		else: 
			s.insert(0, expr[i]) 
	
	# Length of the reduced expression 
	# red_len = (m+n) 
	red_len = len(s) 

	# count opening brackets at the 
	# end of stack 
	n = 0
	while (len(s)and s[0] == '') : 
			s.pop(0) 
			n += 1

	# return ceil(m/2) + ceil(n/2) which 
	# is actually equal to (m+n)/2 + n%2 
	# when m+n is even. 
	return (red_len // 2 + n % 2) 

# Driver Code 
if __name__ == '__main__': 

	expr = " }}}{{{ "
	print(countMinReversals(expr.strip())) 