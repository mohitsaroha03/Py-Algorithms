# Link: https://leetcode.com/problems/relative-sort-array/discuss/797773/simple-python3-o(n)-hash-solution
# IsDone: 0
# QUES
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, 
# and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that 
# the relative ordering of items in arr1 are the same as in arr2.  
# Elements that don't appear in arr2 should be placed at the end of arr1 in
# ALGO
# Loop through A1[], store the count of every number in a HashMap (key: number, value: count of number)
# Loop through A2[], check if it is present in HashMap, if so, put in output array that many times and remove the number from HashMap.
# Sort the rest of the numbers present in HashMap and put in output array.
class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr2_map = {item:0 for item in arr2}
        output = []
        not_in_arr_2 = []
        

        for item in arr1:
            if item in arr2_map:
                arr2_map[item] += 1
            else:
                not_in_arr_2.append(item)
         
        for item in arr2_map:
            output += [item]*arr2_map[item]
        
        output += sorted(not_in_arr_2)
        return output

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
s = Solution()

print(s.relativeSortArray(arr1, arr2)) 