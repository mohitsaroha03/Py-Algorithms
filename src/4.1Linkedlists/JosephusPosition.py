# Link: https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/

# Python code for Josephus Problem 
  
def josephus(n, k): 
  
      if (n == 1): 
          return 1
      else: 
      
      
          # The position returned by  
          # josephus(n - 1, k) is adjusted 
          # because the recursive call 
          # josephus(n - 1, k) considers 
          # the original position  
          # k%n + 1 as position 1  
          return (josephus(n - 1, k) + k-1) % n + 1
  
# Driver Program to test above function 
  
n = 14
k = 2
  
print("recursive The chosen place is ", josephus(n, k)) 
