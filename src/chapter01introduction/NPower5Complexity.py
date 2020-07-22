''


def function(n):
    for i in range(1, n):
		j = i
		while j < i * i:
			j = j + 1
			if j % i == 0:
				for k in range(0, j):
          			print(" * ")

function(10)
