# Link: https://www.geeksforgeeks.org/longest-sub-array-sum-k/
# https://www.youtube.com/watch?v=ufXxc8Vty9A
# IsDone: 0
import collections 

class Solution:
    def subarraysDivByK(self, A, K):
#1)Sum_array to record the sum of items in list A
#   sum_array[i + 1] - sum_array[j] where sum_array[i] is the sum of A[0:i]
#2) sum_array[i]/K = m, sum_array[j]/K = m where j < i => A[j+1, i] is divisible by K
        remainer_count = collections.defaultdict(int)
        remainer_count[0] = 1
        
        total = 0
        count = 0
        for i in range(len(A)):
            num = A[i]
            total += num
            
            remainer = total % K
            
            if remainer in remainer_count:
                count += remainer_count[remainer]
            
            remainer_count[remainer] += 1
        
        return count

# Driver Code 
if __name__ == '__main__': 

	arr = [4,5,0,-2,-3,1 ] 
	n = len(arr) 
	k = 5
	s= Solution()
	print(s.subarraysDivByK(arr, k)) 