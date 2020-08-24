# Link: https://leetcode.com/problems/relative-sort-array/discuss/797773/simple-python3-o(n)-hash-solution
# IsDone: 0

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

# Driver Code 
if __name__ == '__main__': 

	arr = [4, 5, 0, -2, -3, 1] 
	n = len(arr) 
	k = 5

	print(CountSubarrays(arr, n, k)) 