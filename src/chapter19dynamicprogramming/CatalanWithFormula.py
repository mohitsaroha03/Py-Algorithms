# isGFG: , Link: 
# IsDone: 0
catalan = []
 
# 1st term is 1
catalan.append(1)
 
for i in range (1, 1001):
    x = catalan[i - 1] * (4 * i - 2) / (i + 1)
    catalan.append(x)
 
 
def CatalanNumber(n):
    return catalan[n]
    
print CatalanRecursive(4)    
