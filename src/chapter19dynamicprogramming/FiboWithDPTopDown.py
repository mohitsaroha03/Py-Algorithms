# isGFG: , Link: 
# IsDone: 0
fibTable = {1:1, 2:1}
def Fibo(n):
   if n <= 2:
      return 1
   if n in fibTable:
      return fibTable[n]
   else:
      fibTable[n] = Fibo(n - 1) + Fibo(n - 2)
      return fibTable[n]
      
print(Fibo(10))
