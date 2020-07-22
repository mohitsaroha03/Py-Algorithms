''

def reverse_number(n):
	nReverse = n
	s = n.bit_length()
	while(n):
		nReverse <<= 1
		nReverse |= (n & 1)
		s -= 1
		n >>= 1
	nReverse <<= s	
	print nReverse

n = 4
print n
reverse_number(n)
