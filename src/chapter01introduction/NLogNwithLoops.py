# Link: 
# IsDone: 0

def function(n):
	count = 0
	if n <= 0:
		return
	for i in range(1, n):
		j = 1
		while j < n:
			j = j + i
			count = count + 1
	print (count)

function(20)

def Function2(n):
	for i in range(1, n):
		j = 1
		while j <= n:
			j = j * 2
			print("*")

Function2(20)

import math
def function(n):
	for i in range(1, n / 3):
		j = 1
		while j <= n:
			j = j + 4
			print("*")

function(20)
