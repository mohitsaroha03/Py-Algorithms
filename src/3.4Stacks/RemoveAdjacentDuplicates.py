# Link: https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/discuss/832545/Python-Solution-using-Stack
# IsDone: 0
from collections import deque
class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S) == 0:
            return S
        stack = deque()
        for element in S:
            if not stack or stack[-1] != element:
                stack.append(element)
            elif stack and stack[-1] == element:
                stack.pop()
        return ''.join(stack) # learn
s = Solution()
print(s.removeDuplicates(['6', '2', '4', '1', '2', '1', '2', '2', '1']))