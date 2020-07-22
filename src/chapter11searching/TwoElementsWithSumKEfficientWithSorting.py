''

def pair_sum_k_sorting(A, K):
    left = 0
    right = len(A) - 1; 
    while(left < right):
         if(A[left] + A[right] == K):
              return 1
         elif(A[left] + A[right] < K):
              left += 1
         else:
              right -= 1
    return 0
    
A = [1, 4, 45, 6, 10, -8]
A.sort()
print pair_sum_k_sorting(A, 11)
