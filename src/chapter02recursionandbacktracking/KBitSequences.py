''


def range_to_list(k):
	result = []
	for i in range(0, k):
		result.append(str(i))
	return result
	
def base_k_strings(n, k):
	if n == 0: return []
	if n == 1: return range_to_list(k)
	return [ digit + bitstring for digit in base_k_strings(1, k) for bitstring in base_k_strings(n - 1, k)]
print base_k_strings(4, 3)    
