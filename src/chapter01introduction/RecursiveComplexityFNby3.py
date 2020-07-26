# Link: 
# IsDone: 0

def function(n):
	if n <= 0:
		return
	for i in range(1, 3):  # This loop executes 3 times with recursive value of n/3  value
 		function(n / 3)
function(20)

def Function2(n):
	if n <= 0:
		return
	for i in range(1, 3):  # This loop executes 3 times with recursive value of n/3  value
 		Function2(n - 1)
Function2(20)

def Function3(n):
	if n <= 0:
		return
	for i in range(1, 3):  # This loop executes 3 times with recursive value of n/3  value
 		Function3(0.8 * n)
Function3(20)

