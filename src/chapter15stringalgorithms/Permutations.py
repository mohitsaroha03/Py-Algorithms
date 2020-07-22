''

def recursivePermutations(elems, soFar):
    if len(elems) == 0:
        yield soFar
    else:
        for i in range(0, len(elems)):
            for perm in recursivePermutations(elems[0:i] + elems[i + 1:], soFar + [elems[i]]):
                yield perm
		
	
def permutations(elems):
	for perm in recursivePermutations(elems, []):
		print perm		
		
elems = [1, 2, 3]
permutations(elems)

def permutationByIteration(elems):
    level = [elems[0]]
    for i in range(1, len(elems)):
        nList = []
        for item in level:
            nList.append(item + elems[i])
            for j in range(len(item)):
                nList.append(item[0:j] + elems[i] + item[j:])
        level = nList
    return nList
    
elems = [1, 2, 3]
permutations(elems)    
