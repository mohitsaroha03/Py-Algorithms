# Link: https://leetcode.com/problems/valid-sudoku/discuss/805057/Clean-code-Python-(intuitive-solution)
# https://www.geeksforgeeks.org/check-if-given-sudoku-board-configuration-is-valid-or-not/
import math


class Solution:
    def isValidSudoku(self, arr: List[List[str]]) -> bool:
        for i in arr:
            for j in range(len(i)):
                if i[j] == ".":
                    i[j] = 0
                else:
                    i[j] = int(i[j])
                    
        for i in arr:
            if not self.check_row(i):
                return False
        
        for j in range(len(arr[0])):
            if not self.check_column(arr, j):
                return False
        
        grid_length = int(math.sqrt(len(arr[0])))
        for i in range(grid_length):
            for j in range(grid_length):
                if not self.check_sub_matrix(arr, i, j, grid_length):
                    return False
        return True
    
    def check_row(self, arr):
        res = [x for x in arr if x != 0]
        return len(res) == len(set(res))
    
    def check_column(self, arr, j):
        res = []
        for each in arr:
            res.append(each[j])
        res = [x for x in res if x != 0]
        return len(res) == len(set(res))
    
    def check_sub_matrix(self, arr, i, j, grid_size):
        buff = set()
        for ii in range(i * grid_size, (i * grid_size) + grid_size):
            for jj in range(j * grid_size, (j * grid_size) + grid_size):
                if arr[ii][jj] in buff and arr[ii][jj] != 0:
                    return False
                buff.add(arr[ii][jj])
        return True