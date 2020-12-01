# Link: https://www.geeksforgeeks.org/count-entries-equal-to-x-in-a-special-matrix/
# Python 3 program for counting  
# number of cell equals to given x  
  
# function to count factors  
# as number of cell  
def count(n, x): 
    cnt = 0
  
    # traverse and find the factors  
    for i in range(1, n + 1): 
  
        # // x%i == 0 means i is factor of x  
        # x/i <= n means i and j are <= n (for i*j=x)  
        if i <= x: 
            if x // i <= n and x % i == 0: 
                cnt += 1
    return cnt 
  
# Driver code 
n = 8
x = 24
print(count(n, x)) 