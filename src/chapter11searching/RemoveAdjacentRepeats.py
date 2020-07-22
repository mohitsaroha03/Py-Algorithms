''

def removeAdjacentRepeats(nums):
  i = 1
  while i < len(nums):    
    if nums[i] == nums[i - 1]:
      nums.pop(i)
      i -= 1  
    i += 1
  return nums
  
nums = ["A", "B", "C", "C", "C", "C", "B", "A"]  
print removeAdjacent(nums)
