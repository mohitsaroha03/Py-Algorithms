# Link: https://www.geeksforgeeks.org/find-maximum-dot-product-two-arrays-insertion-0s/
# Python 3 program to find maximum dot 
# product of two array 
  
# Function compute Maximum Dot Product  
# and return it 
def MaxDotProduct(A, B, m, n): 
      
    # Create 2D Matrix that stores dot product 
    # dp[i+1][j+1] stores product considering  
    # B[0..i] and A[0...j]. Note that since  
    # all m > n, we fill values in upper  
    # diagonal of dp[][] 
    dp = [[0 for i in range(m + 1)]  
             for j in range(n + 1)] 
  
    # Traverse through all elements of B[] 
    for i in range(1, n + 1, 1): 
          
        # Consider all values of A[] with indexes  
        # greater than or equal to i and compute 
        # dp[i][j] 
        for j in range(i, m + 1, 1): 
              
            # Two cases arise 
            # 1) Include A[j] 
            # 2) Exclude A[j] (insert 0 in B[])  
            dp[i][j] = max((dp[i - 1][j - 1] + 
                            (A[j - 1] * B[i - 1])) ,  
                            dp[i][j - 1]) 
  
    # return Maximum Dot Product 
    return dp[n][m]  
  
# Driver Code 
if __name__ == '__main__': 
    A = [2, 3 , 1, 7, 8] 
    B = [3, 6, 7] 
    m = len(A) 
    n = len(B) 
    print(MaxDotProduct(A, B, m, n)) 