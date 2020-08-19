# Link: https://leetcode.com/problems/relative-sort-array/discuss/797773/simple-python3-o(n)-hash-solution
# IsDone: 0
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
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