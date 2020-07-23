# isGFG: , Link: 
# IsDone: 0
def LongestIncreasingSequence2(numList):
    n = len(numList) 
    LISTable = [1]
    for i in range(1, len(numList))):
        LISTable.append(1)
        for j in range(i + 1, n):
            if numList[i] < numList[j] and LISTable[i] < LISTable[j] + 1:
                LISTable[i] = 1 + LISTable[j]
    print LISTable
    return max(LISTable)

print LongestIncreasingSequence2([3, 2, 6, 4, 5, 1])
