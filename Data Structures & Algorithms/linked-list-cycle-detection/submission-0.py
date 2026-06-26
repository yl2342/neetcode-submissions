# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        s,f = head, head

        # check two since step is 2
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                return True
        return False

        