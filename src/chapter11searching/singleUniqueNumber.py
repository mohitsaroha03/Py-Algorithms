''

class Solution(object):
    def singleNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        for n in A:
            result ^= n
        return result
