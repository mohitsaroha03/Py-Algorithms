''


def function(n):
	count = 0
	for i in range(n / 2, n):  # Outer loop execute n/2 times
		j = 1
		while j + n / 2 <= n:  # Middle loop executes n/2 times
			k = 1
			while k <= n:  # Inner loop execute logn times
				count = count + 1
				k = k * 2
			j = j + 1

	print (count)

function(20)
