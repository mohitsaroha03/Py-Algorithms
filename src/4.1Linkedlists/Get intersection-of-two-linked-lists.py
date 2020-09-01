# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/817777/Python-Solution-O(n)-time-and-O(1)-space-by-modifying-list-in-place
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        cleaner = headB
        while headB:
            headB.val = str(headB.val)
            headB = headB.next
        target = None
        while headA:
            if isinstance(headA.val, str):
                target = headA
                break
            headA = headA.next
        while cleaner:
            cleaner.val = int(cleaner.val)
            cleaner = cleaner.next
        return target