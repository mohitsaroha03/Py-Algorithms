# Link: 
# IsDone: 0
def Fibo(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	return a
      
print(Fibo(10))	  
