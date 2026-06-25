# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #############
        # Iteration #
        #############
        prev, curr = None, head
        while curr:
            temp = curr.next # save where curr.next points as temp
            curr.next = prev # reverse
            prev = curr # move prev to curr
            curr = temp # move curr 1 step forward to previously stored temp
        return prev



        # #############
        # # recursion #
        # #############
        # Key insight: newHead=4 was returned unchanged all the way up the chain. Only head.next.next and head.next were modified in each frame.
        # # base case
        # if not head:
        #     return None
        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None

        # return newHead


        






    
        