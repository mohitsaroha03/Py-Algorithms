# Link: https://www.geeksforgeeks.org/how-to-print-maximum-number-of-a-using-given-four-keys/
# A recursive Python3 program to print maximum  
# number of A's using following four keys 
  
# A recursive function that returns  
# the optimal length string for N keystrokes 
  
def findoptimal(N): 
      
    # The optimal string length is  
    # N when N is smaller than 
    if N<= 6: 
        return N 
  
    # Initialize result  
    maxi = 0
  
    # TRY ALL POSSIBLE BREAK-POINTS  
    # For any keystroke N, we need 
    # to loop from N-3 keystrokes  
    # back to 1 keystroke to find  
    # a breakpoint 'b' after which we  
    # will have Ctrl-A, Ctrl-C and then  
    # only Ctrl-V all the way. 
    for b in range(N-3, 0, -1): 
        curr =(N-b-1)*findoptimal(b) 
        if curr>maxi: 
            maxi = curr 
      
    return maxi 
# Driver program 
if __name__=='__main__': 
      
  
# for the rest of the array we will 
# rely on the previous  
# entries to compute new ones  
    for n in range(1, 21): 
        print('Maximum Number of As with ', n, 'keystrokes is ', findoptimal(n)) 
         