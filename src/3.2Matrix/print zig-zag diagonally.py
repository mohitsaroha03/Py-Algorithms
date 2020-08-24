# https://leetcode.com/problems/diagonal-traverse/discuss/770789/simple-fast-python3-sol
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        lastRow = len(matrix)-1
        lastCol = len(matrix[0])-1
        result = []
        goingDown = False
        totalElems = len(matrix) * len(matrix[0])
        rowId = 0
        colId = 0
        for _ in range(totalElems):
            if rowId <= lastRow and colId <= lastCol:
                result.append(matrix[rowId][colId])
            if goingDown:
                if rowId == lastRow or colId == 0:
                    goingDown = False
                    if colId == 0 and rowId == lastRow:
                        colId += 1
                    elif colId == 0:
                        rowId += 1

                    else:
                        colId += 1
                else:
                    colId -= 1
                    rowId += 1

            else:
                if rowId == 0 or colId == lastCol:
                    goingDown = True
                    if colId == lastCol:
                        rowId += 1
                    else:
                        colId += 1
                else:
                    colId += 1
                    rowId -= 1
                
            
                    
                    
        return result