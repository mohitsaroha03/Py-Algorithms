#

class Solution(object):
    def numberOfConnectedComponents(self, head, S):
        s = set(S)
        current = head
        result = 0
        while current:
            if (current.data in s and
                    getattr(current.next, 'data', None) not in s):
                ans += 1
            current = current.next

        return result

