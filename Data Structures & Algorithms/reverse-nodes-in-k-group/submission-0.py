# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy # starting point, previous node of a group

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth: 
                break # reach the end
            groupNext = kth.next
            # now we can locate the group
            prev, curr = kth.next, groupPrev.next # key: set prev = kth.next
            # within group reverse order
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # now kth is sill the last in the group, need to make it the first
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next




    def getKth(self, curr, k):
        # get the kth node in a group
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        



        