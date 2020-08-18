# Link: 
# IsDone: 0

import math
count = 0
def function(n):
	global count
	if n <= 2:
		return 1
	else: 
		function(round(math.sqrt(n)))
		count = count + 1
		return count

print(function(200))
