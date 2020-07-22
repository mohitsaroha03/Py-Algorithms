''

def KthSmallest (X, K):
     r = X.left.size + 1  # Assume size property is added to node
     if(K == r): 
          return X	
     if(K < r): 
          return KthSmallest (X.left, K)
     if(K > r): 
          return KthSmallest (X.right, K - r)

