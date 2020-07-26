# Link: 
# IsDone: 0

def function(n):
	if (n < 2):  # Constant time
		return
	else:
		counter = 0  # Constant time
	for i in range(1, 8):  # This loop executes 8 times with n value half in every call
		function (n / 2)
	for i in range(1, n ** 3):  # This loop executes n^3 times with constant time loop
		counter = counter + 1